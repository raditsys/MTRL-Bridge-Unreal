MTRL//SCRIPT 1 — compact contract
Return only one complete MTRL_SCRIPT block. Use exact names/pins from AI Context.

MTRL_SCRIPT 1
GRAPH | name
MODE | replace
NODE | id | node name/class | x | y | optional label
FUNCTION | id | exact function name/path | x | y | optional label
SCALAR | id | name | default | x | y
VECTOR | id | name | r,g,b,a | x | y
CONST | id | value | x | y
VEC2/VEC3/VEC4 | id | comma values | x | y
CUSTOM | id | name | CMOT_Float1/2/3/4 | x | y
INPUT | id | pin | optional property
OUTPUT | id | pin | optional index
PROPS | id
ExactProperty=Value
ENDPROPS
CODE | id
HLSL
ENDCODE
LINK | fromId | outputPin | toId | inputPin
END_SCRIPT

RULES
- Prefer native nodes or listed FUNCTIONs; use Custom HLSL only when simpler.
- LINK pins: use catalog names. Validate every LINK before answering.
- Safe fallback: if a requested pin is wrong but that side has exactly ONE pin, MTRL auto-uses it. Unique partial pin matches are also auto-fixed. Never guess an ambiguous multi-pin connection.
- FUNCTION: only use functions listed in AI Context. Exact path is only needed when names collide.
- INPUT/OUTPUT are mainly for Custom/raw nodes. PROPS uses exact UE property names.
- # and // comments are allowed. Unknown commands fail.
