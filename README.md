# MTRL//BRIDGE

**MTRL//BRIDGE** is a free, self-contained browser tool for building Unreal Engine 5.4.x material graphs, generating Unreal Material Editor clipboard text, and turning compact AI-generated `MTRL_SCRIPT 1` recipes into editable node graphs.

It is designed for technical artists who want a fast bridge between an LLM, a visual material graph, and Unreal's Material Editor without requiring a custom Unreal plugin for the core workflow.

> Unofficial community tool. Not affiliated with or endorsed by Epic Games.

## Quick start

MTRL//BRIDGE is primarily designed as an **AI → material graph → Unreal** workflow. On first launch, the compact **Start Here** panel walks through it, and the permanently glowing **Help / Start Here** button always reopens the guide.

1. Download `MTRL_AI_CONTEXT.md` and `MTRL_SCRIPT_PROTOCOL.md` from the Start Here panel.
2. Attach both files to your AI and use the included starter prompt to request a material.
3. Copy the returned `MTRL_SCRIPT 1` recipe and paste it into **AI Build**.
4. Optionally preview/edit the resulting graph in MTRL//BRIDGE.
5. Click **Copy All** or **Copy Selected**, open an Unreal Engine 5.4.x Material graph, and press **Ctrl+V**.

You can also build graphs manually with right-click search and pin wiring. The app autosaves its workspace to browser `localStorage`. For more reliable clipboard permissions, serve the folder locally with `python -m http.server 8080`.

## AI workflow

MTRL//BRIDGE includes a compact AI protocol so ChatGPT or another capable model can generate material graphs for you.

Give the model these two files:

- `MTRL_AI_CONTEXT.md` — exact supported node/function names, pins, and concise usage hints.
- `MTRL_SCRIPT_PROTOCOL.md` — the lightweight recipe syntax.

Then ask for a complete `MTRL_SCRIPT 1` recipe. Paste the result into **AI Build**.

A good generic prompt is:

```text
Read MTRL_AI_CONTEXT.md and MTRL_SCRIPT_PROTOCOL.md and treat them as authoritative.
Create a complete MTRL_SCRIPT 1 recipe for: [describe the material].
Validate node/function names and LINK pins against the context.
Return the finished recipe with minimal extra text.
```

See [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) for the full workflow and an optional `use mtrl` shortcut for ChatGPT.

## Main features

- Visual UE-style material node graph in a single HTML file.
- Unreal clipboard import and export.
- Copy the full graph or only selected nodes.
- Right-click node/function search and wire-drop auto-connect.
- Multi-graph tabs with add, close, rename, and drag reorder.
- Custom HLSL nodes.
- Compact `MTRL//SCRIPT v1` AI Build workflow.
- Packaged UE 5.4.x Material Function catalog with 465 functions.
- Optional custom Material Function catalogs exported from your own UE install.
- Live animated WebGL preview on a sphere or plane.
- Browser-local autosave; no backend required.

## Live preview

The preview evaluates the active graph through **Make Material Attributes** and approximates common channels including Base Color, Metallic, Specular, Roughness, Emissive, Opacity, Opacity Mask, tangent-space Normal, World Position Offset, and Ambient Occlusion.

The preview is intentionally **not** Unreal's material compiler. It translates a useful subset of nodes and Custom HLSL to WebGL for fast visual feedback. Unsupported UE-only features can fail or fall back while Unreal clipboard export remains usable. Use **Copy error** in the preview header to copy the generated shader and full compiler report when debugging.

## Material Functions

The packaged catalog is enabled by default. To use function metadata from your own UE 5.4.x installation, run:

`tools/UE54_EXPORT_MTRL_FUNCTIONS.py`

inside the Unreal Editor with the Python Editor Script Plugin enabled, then import the generated JSON through **More → Import custom functions…**.

See [docs/MATERIAL_FUNCTIONS.md](docs/MATERIAL_FUNCTIONS.md).

## Documentation

- [Quick Start](docs/QUICK_START.md)
- [AI Workflow](docs/AI_WORKFLOW.md)
- [Material Functions](docs/MATERIAL_FUNCTIONS.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [MTRL//SCRIPT Protocol](MTRL_SCRIPT_PROTOCOL.md)
- [AI Context](MTRL_AI_CONTEXT.md)

There is also a **Help** button inside the app with the essential workflow and links to these docs.

## Browser data

MTRL//BRIDGE stores workspace state, app settings, and an optional custom Material Function catalog under `mtrlbridge.*` keys in browser `localStorage`. **More → Reset local data…** clears only those keys. The packaged function catalog is embedded in `index.html` and is not removed.

## Compatibility and limitations

- Target: Unreal Engine **5.4.x**.
- Unreal clipboard text is editor serialization, not a formally documented interchange format. Rare/version-specific expressions may require importing a real node copied from Unreal first.
- The live preview is approximate and does not guarantee parity with Unreal rendering.
- Texture assets referenced by Unreal are not available to the browser renderer; preview adapters may use placeholders.
- Two pins in the packaged engine-function export do not expose stable GUIDs. MTRL//BRIDGE blocks unsafe function export rather than inventing IDs.

## Repository layout

```text
index.html                    Browser application
MTRL_AI_CONTEXT.md            Compact AI-facing node/function catalog
MTRL_SCRIPT_PROTOCOL.md       MTRL//SCRIPT grammar
examples/                     Example recipes
tools/                        Optional Unreal-side utilities
docs/                         User documentation
```

## License

Choose and add a license before publishing if you want to grant explicit reuse/modification rights. No license is included in this prepared package so that the repository owner can choose the terms.
