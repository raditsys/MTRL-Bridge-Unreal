
## V5.5 — lean AI context + safer links

- MTRL//SCRIPT protocol is intentionally tiny (~1.2 KB).
- AI Context is token-optimized: curated node pins/property keys + short Material Function uses, while keeping all packaged functions discoverable.
- AI Build auto-fixes a bad pin name when the node side has exactly one pin.
- AI Build also accepts a unique partial pin-name match. Ambiguous multi-pin mistakes still fail instead of guessing.
- Build status reports how many pin names were auto-fixed, and hard errors list the available pins.
# MTRL//BRIDGE

A self-contained browser tool for authoring and converting Unreal Engine 5.4.x Material Editor node graphs into Unreal's text clipboard format.

## Run

The simplest option is to double-click `index.html`. Clipboard permissions are more reliable on localhost, so for the best experience run:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080` from this folder.

## Workflow

1. Add nodes from the left palette.
2. Grab and move a node from almost anywhere on its box. Only pins and actual form controls are excluded from dragging.
3. Drag from output diamonds to input diamonds to connect nodes.
4. Select a node to edit its Unreal class and serialized properties.
5. Use **Custom HLSL** for a `MaterialExpressionCustom`; add/remove inputs in the inspector and write HLSL in the Code box.
6. Press **Copy for Unreal**, switch to an open Material Editor graph in UE 5.4.x, and paste with Ctrl+V.
7. To bring an existing graph into the browser, copy nodes in Unreal and use **Paste / Import**.


## Unreal-style right-click search

The graph now has a Material Editor-style spawn menu:

- **Right-click empty graph space** to open the node/function search at the mouse cursor.
- Typing filters progressively and focuses the closest matches.
- **Up/Down** changes the highlighted result, **Enter** spawns it, and **Escape** closes the menu.
- Drag a wire from an input/output pin and release it on empty graph space to open the same search in **auto-connect** mode. The chosen node is spawned at the drop point and its first compatible-side pin is connected automatically.
- Middle mouse or **Alt + left drag** pans the graph so right-click is reserved for the Unreal-style context menu.

## UE 5.4 node coverage

This build exposes 291 expression entries: 159 curated templates with useful pins/default properties plus 132 additional UE 5.4 expression classes in **UE 5.4 / Extended**.

The curated set now covers the main Math, Vector/Color, Constant, Parameter, Texture, Coordinate, Utility, Scene, Particle, Distance Field, Switch, Material Attribute, Runtime Virtual Texture, and Material Function expressions.

The extended list exists so obscure/specialized 5.4 expressions are not simply missing. These spawn as editable raw expressions because many specialized nodes have version-specific, asset-dependent, dynamic, or array-based pins. For maximum fidelity with one of those nodes, copy a real instance from UE, import it into MTRL//BRIDGE, then edit/duplicate it there.


## All Engine Material Functions

Material Functions are assets, not ordinary `MaterialExpression` classes. A correct Function Call node needs the function asset path plus the stable IDs of its Function Input and Function Output nodes. Because those IDs belong to the exact Engine assets installed with your UE 5.4.x build, MTRL//BRIDGE uses a one-time catalog sync rather than shipping guessed/stale function metadata.

1. Enable Unreal's **Python Editor Script Plugin** if needed.
2. Run `UE54_EXPORT_MTRL_FUNCTIONS.py` inside the Unreal Editor.
3. The script scans `/Engine/Functions` recursively and writes `Saved/MTRL_Bridge/ue54_material_functions.json` inside the current project.
4. In MTRL//BRIDGE click **Import functions** and select that JSON file. You can also drag the JSON onto the browser tool.
5. The catalog is stored in browser `localStorage`, so the sync normally only needs to be repeated when you change/update the engine install.

After sync, every exported engine Material Function appears in the left palette and the right-click search as a **FUNC** node. Function Call export writes `MaterialFunction`, `FunctionInputs(n)`, `FunctionOutputs(n)`, and the synced input/output GUIDs. Imported Unreal Function Call nodes are also recognized and round-trip as first-class Function nodes.

The AI handoff supports functions with:

```text
FUNCTION | id | Function Name Or /Engine/... asset path | x | y | optional display name
```

`AI Context` includes the currently synced Material Function catalog, so a future chat can choose actual functions and exact pin names instead of guessing.

## Raw Expression

Raw Expression lets you specify any `MaterialExpression...` class, arbitrary serialized property lines, pins, and the expression-property name attached to each input. Imported Unreal clipboard text also keeps unknown expression property lines wherever possible.

## Custom nodes

Custom HLSL nodes export `Code`, `OutputType`, `Description`, and indexed `Inputs(n)` entries. Input names in the browser become the HLSL identifiers used by Unreal's Custom Material Expression.

## Important note

Unreal's clipboard representation is editor serialization rather than a formally documented interchange standard. Complex/rare nodes can contain editor-version-specific properties, so the safest exact workflow for those nodes is: copy a real node from UE → import it → modify/duplicate it in MTRL//BRIDGE → copy back.

## AI Build / MTRL//SCRIPT

This build includes **MTRL//SCRIPT v1**, a compact chat-to-graph protocol. Click **AI Build** and paste a recipe generated in chat; MTRL//BRIDGE creates the nodes, pins, parameters, Custom HLSL, positions, serialized properties, and connections. If the recipe is already on the clipboard, clicking AI Build imports it immediately. Recipe files can also be dragged onto the app.

Click **AI protocol** inside the graph view to see/copy the built-in contract. The same specification is included as `MTRL_SCRIPT_PROTOCOL.md`, with `example_ai_recipe.mtrl` as a working example.

## Multi-selection / partial Unreal copy

The graph now supports Unreal-style chunk editing:

- Left-drag empty canvas to marquee/box select nodes.
- Hold **Shift** to add to the selection. **Ctrl/Cmd** also supports additive/toggle selection.
- Drag any selected node to move the entire selected group.
- **Ctrl/Cmd+A** selects the whole graph.
- Delete/Backspace removes all selected nodes.
- **Copy Selected** exports only highlighted nodes to Unreal. Connections are preserved only when both endpoints are selected; links to unselected nodes are omitted.
- **Copy All** exports the complete graph.

## Giving a fresh AI the right context

`AI Protocol` is the compact MTRL//SCRIPT grammar. It tells an AI how to express a graph, but it does not by itself enumerate or explain every node available in this specific build.

Use **AI Context** for a new chat when you want maximum reliability. It contains the protocol plus a generated catalog of every node in the current build, curated pin/property metadata, and rules for handling extended/raw UE 5.4 expression classes. Common material nodes generally do not need long explanations; obscure/version-specific nodes should be verified against UE 5.4 documentation/source if the assistant has research access, rather than guessed.

## UE 5.4 Material Function catalog — v3 GUID export

UE 5.4's Python wrapper exposes Material Function interface names/types but not the stable `Id` FGuid fields used by Material Function Call pins. `UE54_EXPORT_MTRL_FUNCTIONS.py` v3 works around this by using `ObjectExporterT3D` to serialize each Function Input/Output with Unreal's own text serializer, then reads the hidden `Id=` field from that text.

A successful catalog should report `exporter_version: 3`, `missing_input_guids: 0`, and `missing_output_guids: 0`. MTRL//BRIDGE no longer invents random IDs when a catalog is incomplete; it warns on import and blocks Unreal export for Function Call nodes whose exact GUIDs are missing.

## Packaged vs custom Material Functions

This build contains a packaged UE 5.4.x engine Material Function catalog (465 functions). Leave **Packaged functions ON** to use it. Turn it **OFF** to use the last catalog loaded through **Import custom**. Importing a custom catalog automatically switches packaged mode off. The packaged catalog is built into `index.html`, so it is available even after clearing browser storage.

**Clear local storage** removes MTRL//BRIDGE's saved graph, custom function catalog, and saved app settings, then reloads the app. It only removes keys prefixed with `mtrlbridge.` and does not remove the packaged catalog.

## Multi-graph tabs

MTRL//BRIDGE can keep multiple independent material graphs in one browser workspace. Use `+` to add a tab, `×` to close it, double-click a tab name to rename it, and drag tabs to reorder them. Import, AI Build, UE Text, Copy All, Copy Selected, Frame All, and Load Sample act on the active tab. The workspace is autosaved under `mtrlbridge.workspace`; older single-graph saves are migrated automatically.

## Live material preview

The upper-right preview renders the active graph on a sphere or plane and updates animated graphs continuously. The preview looks for the latest (or selected) **Make Material Attributes** node and evaluates these channels: Base Color, Metallic, Specular, Roughness, Emissive Color, Opacity, Opacity Mask, Normal, World Position Offset, and Ambient Occlusion. Normal is treated as tangent-space in the preview. `Time` updates every frame and a Pause/Play control is provided.

The preview is intentionally an approximation, not Unreal Engine's material compiler. The browser converts a practical subset of native MTRL nodes and simple Custom HLSL to a WebGL shader. Common math, parameters, UVs, panners/rotators, procedural texture placeholders, Fresnel, SphereMask, Noise, and several common Material Functions have preview adapters. Unsupported Unreal-only expressions/functions fall back instead of blocking graph authoring; UE clipboard export remains independent of preview support.

### V5.1 preview compatibility
Custom HLSL preview translation now maps HLSL `atan2` and `clamp` through GLSL ES-safe overload helpers, including scalar/vector mixed arguments and integer literals. It also maps `ddx`, `ddy`, `rsqrt`, and strips HLSL `f` numeric suffixes. Unreal clipboard export is unchanged.


## V5.3 preview fix
- GLSL scalar literals are now emitted as floats (`0.0`, `1.0`) instead of integers when used by the preview compiler. This fixes WebGL `clamp` overload failures caused by default material channel values.


## V5.4 preview fixes
- Custom HLSL preview strips HLSL compiler attributes such as `[unroll]`/`[loop]`.
- Common C-style casts such as `(float)j` are converted to GLSL constructor casts.
- Live preview header includes **Copy error**, which copies the full compiler log, graph summary, warnings, and numbered generated vertex/fragment shader source.
