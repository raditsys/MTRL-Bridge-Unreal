# AI Workflow

MTRL//BRIDGE uses two small source-of-truth files for AI generation:

- `MTRL_AI_CONTEXT.md` — exact nodes, Material Functions, pins, and concise usage hints.
- `MTRL_SCRIPT_PROTOCOL.md` — compact syntax for building a graph.

You do **not** need to provide the README to the model for normal material generation.

## Generic prompt

Attach/provide both files and use:

```text
Read MTRL_AI_CONTEXT.md and MTRL_SCRIPT_PROTOCOL.md and treat them as authoritative.
Create a complete valid MTRL_SCRIPT 1 recipe for: [YOUR MATERIAL REQUEST].
Validate node names, function names, and LINK pins against the context.
Prefer native Unreal nodes/material functions where practical; use Custom HLSL when it materially simplifies the graph.
Return the finished recipe with minimal extra text.
```

Paste the result into **AI Build**.

## Optional ChatGPT shortcut

If you keep the two files in ChatGPT Library, you can define a short personal trigger such as:

```text
USE MTRL: When I say "use mtrl", read the latest MTRL_AI_CONTEXT and MTRL_SCRIPT_PROTOCOL files from my MTRL Instructions Library folder before generating anything. Treat those files as authoritative and ignore older remembered MTRL syntax. Create a complete valid MTRL_SCRIPT 1 recipe, validate node/function names and LINK pins against the context, and return the finished recipe with minimal extra text.
```

Then requests can be as short as:

```text
use mtrl - make a wet moss material with world-aligned breakup and animated drips
```

This Library workflow is optional. Any model can use MTRL if it can read the two files and follow the protocol.

## Why there are two files

The protocol stays tiny so the grammar is cheap to process. The AI Context contains the current build's exact catalog and is generated/updated alongside the tool. This avoids baking a large, quickly-stale node catalog into a permanent prompt or memory.

## Error-resistant behavior

The current parser automatically repairs safe pin-name mistakes when a node side has exactly one pin and accepts a unique partial pin-name match. Ambiguous multi-pin mistakes still fail rather than silently connecting the wrong pin.

If AI Build rejects a recipe, use the error's **Available pins** list to correct the specific `LINK` line.

## Sharing an issue

For an AI Build problem, share:

1. The complete `MTRL_SCRIPT 1` recipe.
2. The exact AI Build error.
3. The MTRL//BRIDGE version/build you are using.

For a live preview shader problem, click **Copy error** and share the full report; it includes numbered generated shader source.
