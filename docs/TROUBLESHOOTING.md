# Troubleshooting

## Paste into Unreal does nothing

Make sure an Unreal Engine 5.4.x **Material graph** has focus before pressing Ctrl+V. If browser clipboard access is blocked, run MTRL//BRIDGE from localhost with `python -m http.server 8080`.

## AI Build says a pin was not found

The recipe used a pin name that does not exist on that node. Current builds auto-fix safe single-pin mistakes and unique partial matches, but deliberately reject ambiguous multi-pin guesses.

Read the **Available pins** shown in the error and update that `LINK` line. The AI should be using the current `MTRL_AI_CONTEXT.md` and `MTRL_SCRIPT_PROTOCOL.md`.

## Live preview says "connect to Make Material Attributes"

The WebGL renderer needs a clear material root. Connect the branches you want to preview into **Make Material Attributes**. The node does not need to connect to anything after that.

## Live preview shader compile error

The browser preview translates a subset of UE/HLSL behavior to WebGL GLSL. Unreal export can still be valid even when the browser preview cannot translate a feature.

Click **Copy error** in the preview header. The copied report includes:

- Raw WebGL compiler/linker error
- Active graph information
- Connected material channels
- Preview warnings
- Custom HLSL
- Numbered generated vertex shader
- Numbered generated fragment shader

Include that report when filing an issue.

## Function call export is blocked

The selected Material Function has an incomplete/missing stable pin GUID in the active catalog. MTRL//BRIDGE blocks unsafe output instead of generating a fake GUID. Try the packaged catalog or export a fresh custom catalog from your Unreal installation.

## I want to clear everything saved in the browser

Choose **More → Reset local data…**. Only `mtrlbridge.*` localStorage keys are removed.

## Rare Unreal node is missing or inaccurate

Specialized expressions can have dynamic, asset-dependent, or version-specific serialization. Copy a real instance from Unreal, use **Paste / Import**, then edit or duplicate the imported node in MTRL//BRIDGE.
