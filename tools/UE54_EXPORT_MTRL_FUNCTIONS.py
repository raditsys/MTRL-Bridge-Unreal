"""
MTRL//BRIDGE — Unreal Engine 5.4.x Material Function catalog exporter (v3)

Run inside Unreal Editor with the Python Editor Script Plugin enabled.
Writes:
    <Project>/Saved/MTRL_Bridge/ue54_material_functions.json

UE 5.4 exposes Material Function input/output names and types to Python, but the
stable FGuid `Id` used by MaterialFunctionCall pins is not exposed in the Python
wrapper. v3 uses reflection for metadata and Unreal's native ObjectExporterT3D
for those hidden Id fields.
"""
import json, os, re, unreal

ROOT = "/Engine/Functions"
OUT_DIR = os.path.join(unreal.Paths.project_saved_dir(), "MTRL_Bridge")
OUT_FILE = os.path.join(OUT_DIR, "ue54_material_functions.json")
TEMP_T3D = os.path.join(OUT_DIR, "_mtrl_guid_probe.t3d")

def _prop(obj, name, default=None):
    if obj is None: return default
    try: return obj.get_editor_property(name)
    except Exception: pass
    try: return getattr(obj, name)
    except Exception: return default

def _guid_text(value):
    if value is None: return ""
    text = str(value)
    m = re.search(r"(?<![0-9A-Fa-f])([0-9A-Fa-f]{32})(?![0-9A-Fa-f])", text)
    if m: return m.group(1).upper()
    m = re.search(r"([0-9A-Fa-f]{8})-([0-9A-Fa-f]{4})-([0-9A-Fa-f]{4})-([0-9A-Fa-f]{4})-([0-9A-Fa-f]{12})", text)
    if m: return "".join(m.groups()).upper()
    words = re.findall(r"(?<![0-9A-Fa-f])([0-9A-Fa-f]{8})(?![0-9A-Fa-f])", text)
    return "".join(words[-4:]).upper() if len(words) >= 4 else ""

def _package_key(obj):
    try:
        outermost = obj.get_outermost()
        if outermost: return outermost.get_path_name()
    except Exception: pass
    path = obj.get_path_name() if obj else ""
    return path.split(".", 1)[0]

def _belongs(obj, asset):
    try:
        if obj.get_typed_outer(unreal.MaterialFunction) == asset: return True
    except Exception: pass
    return _package_key(obj) == _package_key(asset)

def _category(asset, path):
    raw = _prop(asset, "library_categories_text", []) or []
    cats = [str(x).strip() for x in raw if str(x).strip()]
    if cats: return " / ".join(cats)
    package = path.split(".", 1)[0]
    parent = package.rsplit("/", 1)[0]
    rel = parent[len(ROOT):].strip("/") if parent.startswith(ROOT) else ""
    return rel or "Engine"

def _native_export_text(obj):
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
        if os.path.exists(TEMP_T3D): os.remove(TEMP_T3D)
        task = unreal.AssetExportTask()
        task.set_editor_property("object", obj)
        task.set_editor_property("filename", TEMP_T3D)
        task.set_editor_property("automated", True)
        task.set_editor_property("prompt", False)
        task.set_editor_property("replace_identical", True)
        task.set_editor_property("write_empty_files", True)
        task.set_editor_property("exporter", unreal.ObjectExporterT3D())
        if not unreal.Exporter.run_asset_export_task(task): return ""
        if not os.path.exists(TEMP_T3D): return ""
        with open(TEMP_T3D, "r", encoding="utf-8", errors="replace") as f: return f.read()
    except Exception as exc:
        unreal.log_warning("MTRL//BRIDGE v3: T3D probe failed for {}: {}".format(getattr(obj, 'get_path_name', lambda:'?')(), exc))
        return ""

def _hidden_id(exp):
    direct = _guid_text(_prop(exp, "id", None))
    if direct: return direct
    text = _native_export_text(exp)
    if not text: return ""
    m = re.search(r"(?:^|\n)\s*Id\s*=\s*([^\r\n]+)", text, re.I)
    return _guid_text(m.group(1)) if m else ""

def _load_functions():
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    data = reg.get_assets_by_path(unreal.Name(ROOT), recursive=True, include_only_on_disk_assets=False) or []
    out=[]
    for i,d in enumerate(data):
        try:
            a=d.get_asset()
            if a and isinstance(a, unreal.MaterialFunction): out.append(a)
        except Exception as exc: unreal.log_warning("MTRL//BRIDGE v3: load failed {}: {}".format(str(d),exc))
        if i and i%100==0: unreal.log("MTRL//BRIDGE v3: loaded {}/{} assets...".format(i,len(data)))
    return out,len(data)

def _collect(functions):
    wanted={_package_key(a) for a in functions}
    ins={k:[] for k in wanted}; outs={k:[] for k in wanted}; scanned=0
    for obj in unreal.ObjectIterator():
        scanned+=1
        try:
            if isinstance(obj, unreal.MaterialExpressionFunctionInput):
                k=_package_key(obj)
                if k in wanted: ins[k].append(obj)
            elif isinstance(obj, unreal.MaterialExpressionFunctionOutput):
                k=_package_key(obj)
                if k in wanted: outs[k].append(obj)
        except Exception: pass
    return ins,outs,scanned

def _input(exp):
    return {"name":str(_prop(exp,"input_name","Input")),"guid":_hidden_id(exp),"type":str(_prop(exp,"input_type","")),"sort":int(_prop(exp,"sort_priority",0) or 0),"description":str(_prop(exp,"description","") or "")}

def _output(exp):
    return {"name":str(_prop(exp,"output_name","Output")),"guid":_hidden_id(exp),"sort":int(_prop(exp,"sort_priority",0) or 0),"description":str(_prop(exp,"description","") or "")}

def _record(asset,ins,outs):
    path=asset.get_path_name(); k=_package_key(asset)
    input_objs=[o for o in ins.get(k,[]) if _belongs(o,asset)]
    output_objs=[o for o in outs.get(k,[]) if _belongs(o,asset)]
    inputs=[_input(o) for o in input_objs]; outputs=[_output(o) for o in output_objs]
    inputs.sort(key=lambda p:(p["sort"],p["name"].lower())); outputs.sort(key=lambda p:(p["sort"],p["name"].lower()))
    asset_name=asset.get_name(); caption=str(_prop(asset,"user_exposed_caption","") or "").strip()
    return {"name":caption or asset_name,"asset_name":asset_name,"path":path,"category":_category(asset,path),"description":str(_prop(asset,"description","") or ""),"caption":caption,"exposed":bool(_prop(asset,"expose_to_library",False)),"inputs":inputs,"outputs":outputs}

def _probe(functions,ins,outs):
    for a in functions:
        k=_package_key(a)
        for exp in ins.get(k,[])+outs.get(k,[]):
            if not _belongs(exp,a): continue
            g=_hidden_id(exp)
            if g:
                unreal.log("MTRL//BRIDGE v3: native GUID probe OK: {} -> {}".format(exp.get_path_name(),g))
                return True
            unreal.log_error("MTRL//BRIDGE v3: native T3D serializer did not expose Id= for {}".format(exp.get_path_name()))
            return False
    unreal.log_error("MTRL//BRIDGE v3: no FunctionInput/FunctionOutput object available for GUID probe.")
    return False

def main():
    unreal.log("MTRL//BRIDGE v3: scanning {} ...".format(ROOT))
    functions, discovered=_load_functions()
    unreal.log("MTRL//BRIDGE v3: loaded {} Material Functions from {} assets.".format(len(functions),discovered))
    ins,outs,scanned=_collect(functions)
    unreal.log("MTRL//BRIDGE v3: inspected {} loaded UObjects for function interfaces.".format(scanned))
    if not _probe(functions,ins,outs):
        unreal.log_error("MTRL//BRIDGE v3: aborted before writing a bad catalog.")
        return None
    records=[]; skipped=0
    for i,a in enumerate(functions):
        try: records.append(_record(a,ins,outs))
        except Exception as exc:
            skipped+=1; unreal.log_warning("MTRL//BRIDGE v3: skipped {}: {}".format(a.get_path_name(),exc))
        if i and i%25==0: unreal.log("MTRL//BRIDGE v3: processed {}/{} functions...".format(i,len(functions)))
    records.sort(key=lambda f:(f["category"].lower(),f["name"].lower(),f["path"].lower()))
    total_in=sum(len(f["inputs"]) for f in records); total_out=sum(len(f["outputs"]) for f in records)
    miss_in=sum(1 for f in records for p in f["inputs"] if not p["guid"]); miss_out=sum(1 for f in records for p in f["outputs"] if not p["guid"])
    empty=sum(1 for f in records if not f["inputs"] and not f["outputs"])
    payload={"format":"MTRL_FUNCTION_CATALOG","version":1,"exporter_version":3,"engine_hint":"Unreal Engine 5.4.x","root":ROOT,"function_count":len(records),"input_count":total_in,"output_count":total_out,"missing_input_guids":miss_in,"missing_output_guids":miss_out,"empty_interfaces":empty,"functions":records}
    os.makedirs(OUT_DIR,exist_ok=True)
    with open(OUT_FILE,"w",encoding="utf-8") as f: json.dump(payload,f,indent=2,ensure_ascii=False)
    try:
        if os.path.exists(TEMP_T3D): os.remove(TEMP_T3D)
    except Exception: pass
    unreal.log("MTRL//BRIDGE v3: exported {} Material Functions; {} inputs; {} outputs.".format(len(records),total_in,total_out))
    unreal.log("MTRL//BRIDGE v3: wrote {}".format(OUT_FILE))
    if miss_in or miss_out:
        unreal.log_error("MTRL//BRIDGE v3: {} input and {} output GUIDs are still missing. Do not use this catalog for exact function-call export.".format(miss_in,miss_out))
    else:
        unreal.log("MTRL//BRIDGE v3: SUCCESS — all function pin GUIDs recovered.")
    if skipped: unreal.log_warning("MTRL//BRIDGE v3: {} functions skipped.".format(skipped))
    return OUT_FILE

if __name__ == "__main__": main()
