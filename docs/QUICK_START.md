# Quick Start

## 1. Give your AI the MTRL instructions

From **Help / Start Here**, download:

- `MTRL_AI_CONTEXT.md`
- `MTRL_SCRIPT_PROTOCOL.md`

Attach both to your AI, copy the starter prompt from MTRL//BRIDGE, replace `[describe material]`, and ask it to generate the shader/material.

## 2. Build the generated recipe

Copy the returned `MTRL_SCRIPT 1` block, click **AI Build**, paste it, and build the graph.

The two instruction files are the source of truth. The README is not required by the AI.

## 3. Preview and send to Unreal

For the full browser preview, connect the graph into **Make Material Attributes** and use Sphere / Plane. The preview is an approximation of Unreal rendering.

Use **Copy All** for the active graph or **Copy Selected** for only highlighted nodes. Open a Material graph in Unreal Engine 5.4.x and press **Ctrl+V**.

To bring Unreal nodes back into MTRL//BRIDGE, copy them in Unreal and use **Paste / Import**.

## Manual graph editing

Manual authoring is optional:

- Right-click empty graph space: search/add a node or Material Function
- Drag output diamonds to input diamonds: connect
- Drop a wire on empty space: search and auto-connect a new node
- Mouse wheel: zoom
- Middle mouse or Alt + left drag: pan
- Box-drag empty space: select groups
- Shift/Ctrl/Cmd: add/toggle selection
- Delete/Backspace: delete selection
- Tabs: multiple material graphs; double-click rename, drag reorder

## Material Functions

Leave **Packaged functions ON** for the built-in UE 5.4.x catalog. Use **More → Import custom functions…** to use a catalog exported from your own engine installation.

## Troubleshooting

If the live preview reports a shader error, click **Copy error** and share the complete report. If AI Build rejects a recipe, share the recipe plus the exact build error.

**More → Reset local data…** clears MTRL//BRIDGE autosave/settings/custom functions without removing the packaged function catalog.
