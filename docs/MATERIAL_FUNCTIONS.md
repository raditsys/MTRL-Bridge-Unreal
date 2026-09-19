# Material Functions

MTRL//BRIDGE ships with a packaged Unreal Engine 5.4.x Material Function catalog so most users can use engine functions immediately.

## Packaged functions

Keep **Packaged functions ON** to use the built-in catalog. Functions appear in the left palette and right-click search.

A Material Function Call needs the asset path plus stable input/output GUIDs. MTRL//BRIDGE uses real exported metadata and refuses to invent missing GUIDs.

## Export a catalog from your own Unreal installation

Use `tools/UE54_EXPORT_MTRL_FUNCTIONS.py` when you want metadata from your exact UE 5.4.x install.

1. Enable Unreal's **Python Editor Script Plugin**.
2. Run `UE54_EXPORT_MTRL_FUNCTIONS.py` inside the Unreal Editor.
3. The exporter scans `/Engine/Functions` and writes a JSON catalog under your project's `Saved/MTRL_Bridge/` folder.
4. In MTRL//BRIDGE choose **More → Import custom functions…** and select the JSON file.
5. Packaged mode automatically turns off so the custom catalog becomes active.

Turn **Packaged functions ON** at any time to switch back to the embedded catalog.

## Browser storage

The custom catalog is stored in browser `localStorage`. Resetting local data removes the custom catalog but not the packaged catalog embedded in `index.html`.

## AI usage

`MTRL_AI_CONTEXT.md` includes concise function descriptions plus exact input/output names so an AI can choose existing Material Functions instead of rebuilding everything from primitive nodes.
