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


CATALOG LEGEND
N|name|I:inputs|O:outputs|P:optional property keys
F|name|brief use|I:inputs|O:outputs
* after I/O = exactly one pin; generic Input/Output is safe because MTRL resolves sole pins.

NODES
N|Add|I:A,B|O:Output|P:ConstA,ConstB
N|Multiply|I:A,B|O:Output|P:ConstA,ConstB
N|Subtract|I:A,B|O:Output|P:ConstA,ConstB
N|Divide|I:A,B|O:Output|P:ConstA,ConstB
N|Lerp|I:A,B,Alpha|O:Output|P:ConstA,ConstB,ConstAlpha
N|Inverse Lerp|I:A,B,Value|O:Output
N|Clamp|I:Input,Min,Max|O:Output|P:MinDefault,MaxDefault
N|Saturate|I:Input|O:Output
N|One Minus|I:Input|O:Output
N|Abs|I:Input|O:Output
N|Ceil|I:Input|O:Output
N|Floor|I:Input|O:Output
N|Frac|I:Input|O:Output
N|Round|I:Input|O:Output
N|Truncate|I:Input|O:Output
N|Sign|I:Input|O:Output
N|Square Root|I:Input|O:Output
N|Normalize|I:Input|O:Output
N|Length|I:Input|O:Output
N|Min|I:A,B|O:Output
N|Max|I:A,B|O:Output
N|Fmod|I:A,B|O:Output
N|Dot Product|I:A,B|O:Output
N|Cross Product|I:A,B|O:Output
N|Distance|I:A,B|O:Output
N|Step|I:Y,X|O:Output
N|SmoothStep|I:Min,Max,Value|O:Output
N|Power|I:Base,Exp|O:Output|P:ConstExponent
N|Exp|I:Input|O:Output
N|Exp2|I:Input|O:Output
N|Log|I:Input|O:Output
N|Log2|I:Input|O:Output
N|Log10|I:Input|O:Output
N|Sine|I:Input|O:Output|P:Period
N|Cosine|I:Input|O:Output|P:Period
N|Arcsine|I:Input|O:Output
N|Arccosine|I:Input|O:Output
N|Arctangent|I:Input|O:Output
N|Arctangent2|I:Y,X|O:Output
N|Arcsine Fast|I:Input|O:Output
N|Arccosine Fast|I:Input|O:Output
N|Arctangent Fast|I:Input|O:Output
N|Arctangent2 Fast|I:Y,X|O:Output
N|If|I:A,B,A > B,A = B,A < B|O:Output|P:EqualsThreshold
N|DDX|I:Input|O:Output
N|DDY|I:Input|O:Output
N|Derive Normal Z|I:Input|O:Output
N|Constant Bias Scale|I:Input|O:Output|P:Bias,Scale
N|Append Vector|I:A,B|O:Output
N|Append 3 Vector|I:A,B,C|O:Output
N|Append 4 Vector|I:A,B,C,D|O:Output
N|Component Mask|I:Input|O:Output|P:R,G,B,A
N|Desaturation|I:Input,Fraction|O:Output|P:LuminanceFactors
N|BlackBody|I:Temp|O:Output
N|RGB to HSV|I:Input|O:Output
N|HSV to RGB|I:Input|O:Output
N|SRGB to Working Color Space|I:Input|O:Output
N|Constant|I:-|O:Output|P:R
N|Constant 2|I:-|O:Output|P:R,G
N|Constant 3|I:-|O:Output|P:Constant
N|Constant 4|I:-|O:Output|P:Constant
N|Static Bool|I:-|O:Output|P:Value
N|Scalar Parameter|I:-|O:Output|P:DefaultValue,ParameterName,ExpressionGUID
N|Vector Parameter|I:-|O:Output|P:DefaultValue,ParameterName,ExpressionGUID
N|Static Bool Parameter|I:-|O:Output|P:DefaultValue,ParameterName,ExpressionGUID
N|Static Switch Parameter|I:True,False|O:Output|P:DefaultValue,ParameterName,ExpressionGUID
N|Static Component Mask Parameter|I:Input|O:Output|P:DefaultR,DefaultG,DefaultB,DefaultA,ParameterName,ExpressionGUID
N|Channel Mask Parameter|I:Input|O:Output|P:ParameterName,ExpressionGUID
N|Collection Parameter|I:-|O:Output|P:ParameterName
N|Dynamic Parameter|I:-|O:Param1,Param2,Param3,Param4
N|Texture Sample|I:UVs,Texture Object,Mip Value,DDX,DDY|O:RGB,R,G,B,A|P:SamplerType
N|Texture Sample Parameter 2D|I:UVs,Mip Value,DDX,DDY|O:RGB,R,G,B,A|P:ParameterName,SamplerType,ExpressionGUID
N|Texture Sample Parameter Cube|I:UVW,Mip Value|O:RGB,R,G,B,A|P:ParameterName,SamplerType,ExpressionGUID
N|Texture Sample Parameter Volume|I:UVW,Mip Value|O:RGB,R,G,B,A|P:ParameterName,SamplerType,ExpressionGUID
N|Texture Object|I:-|O:Texture Object|P:SamplerType
N|Texture Object Parameter|I:-|O:Texture Object|P:ParameterName,SamplerType,ExpressionGUID
N|Texture Property|I:Texture Object|O:Output|P:Property
N|Antialiased Texture Mask|I:UVs|O:Output|P:Threshold,Channel
N|Texture Coordinate|I:-|O:UV|P:CoordinateIndex,UTiling,VTiling
N|Panner|I:UVs,Time,Speed|O:Output|P:SpeedX,SpeedY,ConstCoordinate
N|Rotator|I:UVs,Time|O:Output|P:CenterX,CenterY,Speed
N|Bump Offset|I:UVs,Height|O:Output|P:HeightRatio,ReferencePlane,ConstCoordinate
N|World Position|I:-|O:XYZ
N|Actor Position WS|I:-|O:XYZ
N|Object Position WS|I:-|O:XYZ
N|Camera Position WS|I:-|O:XYZ
N|Camera Vector WS|I:-|O:XYZ
N|Reflection Vector WS|I:Custom Reflection Vector|O:XYZ
N|Pixel Normal WS|I:-|O:XYZ
N|Vertex Normal WS|I:-|O:XYZ
N|Vertex Tangent WS|I:-|O:XYZ
N|Pre-Skinned Position|I:-|O:XYZ
N|Pre-Skinned Normal|I:-|O:XYZ
N|Object Orientation|I:-|O:XYZ
N|Object Radius|I:-|O:Radius
N|Object Bounds|I:-|O:XYZ
N|Pre-Skinned Local Bounds|I:-|O:Min,Max,Extent,Size
N|Lightmap UVs|I:-|O:UV
N|Screen Position|I:-|O:ViewportUV
N|View Size|I:-|O:ViewSize,InvViewSize
N|Transform Vector|I:Input|O:Output|P:TransformSourceType,TransformType
N|Transform Position|I:Input|O:Output|P:TransformSourceType,TransformType
N|Rotate About Axis|I:Normalized Rotation Axis,Rotation Angle,Pivot Point,Position|O:Result
N|Time|I:-|O:Output
N|Delta Time|I:-|O:Output
N|Two Sided Sign|I:-|O:Output
N|Vertex Color|I:-|O:RGB,R,G,B,A
N|Per Instance Random|I:-|O:Output
N|Per Instance Fade|I:-|O:Output
N|Per Instance Custom Data|I:Default Value|O:Output|P:DataIndex,DefaultValue|U:Reads per-instance custom primitive/instance da…
N|Previous Frame Switch|I:Current Frame,Previous Frame|O:Output|U:Selects current-frame versus previous-frame dat…
N|Sphere Mask|I:A,B,Radius,Hardness|O:Output|P:AttenuationRadius,HardnessPercent
N|Fresnel|I:Exponent,Base Reflect Fraction,Normal|O:Output|P:Exponent,BaseReflectFraction
N|Noise|I:Position,Filter Width|O:Output|P:Scale,Quality,Levels,OutputMin,OutputMax
N|Vector Noise|I:Position|O:Output|P:Quality,NoiseFunction
N|Reroute|I:Input|O:Output
N|Custom HLSL|I:Input0|O:Output|P:Description,OutputType|U:Arbitrary HLSL expression.
N|Scene Texture|I:UV|O:Color,Size,InvSize|P:SceneTextureId|U:Reads a selected scene texture; availability de…
N|Scene Color|I:UV|O:Color|P:InputMode
N|Scene Depth|I:UV|O:Depth|P:InputMode
N|Pixel Depth|I:-|O:Depth
N|Depth Fade|I:Opacity,Fade Distance|O:Output|P:FadeDistanceDefault
N|Distance Cull Fade|I:-|O:Output
N|Eye Adaptation|I:-|O:Output
N|Eye Adaptation Inverse|I:Light Value,Alpha|O:Output
N|Decal Color|I:-|O:RGB
N|Decal Lifetime Opacity|I:-|O:Output
N|Particle Color|I:-|O:RGB,R,G,B,A
N|Particle Position WS|I:-|O:XYZ
N|Particle Direction|I:-|O:XYZ
N|Particle Radius|I:-|O:Radius
N|Particle Random|I:-|O:Output
N|Particle Relative Time|I:-|O:Output
N|Particle Size|I:-|O:XY
N|Particle Speed|I:-|O:Speed
N|Particle Sprite Rotation|I:-|O:Output
N|Particle Macro UV|I:-|O:UV
N|Distance To Nearest Surface|I:Position|O:Distance|U:Global distance-field distance query; requires…
N|Distance Field Gradient|I:Position|O:Gradient|U:Global distance-field gradient/direction query.
N|Distance Field Approx AO|I:Position,Normal|O:AO
N|Quality Switch|I:Default,Low,High,Epic|O:Output
N|Feature Level Switch|I:Default|O:Output
N|Shading Path Switch|I:Default,Deferred,Forward|O:Output
N|Ray Tracing Quality Switch|I:Normal,Ray Traced|O:Output
N|Nanite Replace|I:Default,Nanite|O:Output
N|Lightmass Replace|I:Realtime,Lightmass|O:Output
N|Shadow Replace|I:Default,Shadow|O:Output
N|Make Material Attributes|I:Base Color,Metallic,Specular,Roughness,Emissive Color,Opacity,Opacity Mask,Normal,World Position Offset,Ambient Occlusion,Pixel Depth Offset|O:Material Attributes|U:Builds a Material Attributes struct from indivi…
N|Break Material Attributes|I:Material Attributes|O:Base Color,Metallic,Specular,Roughness,Emissive Color,Opacity,Opacity Mask,Normal,World Position Offset,Ambient Occlusion,Pixel Depth Offset|U:Extracts channels from a Material Attributes st…
N|Blend Material Attributes|I:A,B,Alpha|O:Material Attributes
N|Get Material Attributes|I:Material Attributes|O:Output|U:Extracts selected fields from a Material Attrib…
N|Set Material Attributes|I:Material Attributes|O:Material Attributes|U:Overwrites selected fields of a Material Attrib…
N|Runtime Virtual Texture Sample|I:UV,World Position|O:Base Color,Specular,Roughness,Normal,World Height,Mask|U:Samples an assigned Runtime Virtual Texture; as…
N|Runtime Virtual Texture Output|I:Base Color,Specular,Roughness,Normal,World Height,Opacity,Mask|O:-
N|Runtime Virtual Texture Replace|I:Default,Virtual Texture|O:Output
N|Function Input|I:-|O:Output|P:InputName,InputType
N|Function Output|I:Input|O:-|P:OutputName
N|Material Function Call|I:-|O:Output
N|Raw Expression|I:A,B|O:Output

RAW NODES
Exact UE 5.4 MaterialExpression class names are allowed. For raw nodes, declare exact INPUT/OUTPUT/PROPS; do not invent unknown pins.

FUNCTIONS
F|DespillByAvg|Despill using average color of input|I:*|O:*
F|DespillManual|Manual despill function|I:Image Color,KeyedColor,Despill Minimum,Despill Divisor,Despill Amount,Sky Color,Sky Intensity,Raw Comparison|O:*
F|DiffColorKeyerErodeSinglePass|Color difference based keyer|I:IsExternalSource,Texture2D,TextureExternal,KeyColor,AlphaThreshold,AlphaOffset,WeightRed,WeightBlue,ClipBlack,ClipWhite,UnPremult,---------------------,ErodeAlpha,KernalSize,NumSamples|O:Alpha,RGB
F|LinearTosRGB|Convert Linear to sRGB|I:*|O:*
F|sRGBToLinear|Convert sRGB to Linear|I:*|O:*
F|1Dto2DIndex|Converts a 2D index into a 1D index based on a given to…|I:1D Index,Cells XY|O:2D Index,Centered UV Position
F|1Dto3DIndex|Converts a 2D index into a 1D index based on a given to…|I:1D Index,Cells XYZ|O:3D Index,Centered UV Position
F|2Dto1DIndex|Converts a 2D index into a 1D index based on a given to…|I:2D Index,Columns X|O:1D Index,Centered UV Position
F|3Dto1DIndex|Converts a 3D index into a 1D index based on a given to…|I:3D Index,Cells XYZ|O:1D Index,Centered UVW Position
F|ObjectAlignedVirtualPlaneCoordinates|Draws 2d coordinate at a specified alignment and positi…|I:Projection Pivot Position,Plane Depth Offset,Coordinate Scale (WS),World Space Projection Normal,World Space Projection Tangent,World Space Projection Binormal|O:Center Aligned UV Plane,Non Biased Coordinates
F|WorldSpaceAlignedScreenCoordinates|Moves the center of screen aligned coordinates to the c…|I:*|O:Offset UVs,Offset and Scaled UVS
F|CameraVectorToLatLongUV|Converts camera vector to latlong UVs.|I:*|O:*
F|InteriorCubemap|Interior Cubemap conforms a cubemap to be in the form o…|I:UVs,Tiling,Randomize Rotation|O:*
F|DebugBinaryValues-Float|Displays the bit pattern of the input value as a floati…|I:Number To Convert,Number of Bits,UVs|O:*
F|DebugBinaryValues-Int|Displays the bit pattern of the input value as a floati…|I:Number To Convert,Number of Bits,UVs|O:*
F|ApplyDBuffer|Apply DBuffer directly to material attributes.|I:InMaterial,DBufferA,DBufferB,DBufferC|O:*
F|StaticMeshDecal_Function|Use this function with "1x1x1_Box_Pivot_-XYZ" to draw d…|I:XYZ Opacity Falloff Hardness,Camera Clip Mask Distance,Local Projection Angle Mask Vector And Falloff Power (V4)|O:0-1 RGB UVW,Combined Mask,Extent bounds masks,Camera Clip Mask,Projection Angle Mask
F|BeersLaw|Returns e^(-d) which is a standard exponential density…|I:Thickness,Depth Scale|O:*
F|RayMarchHeightMap|This function Ray Marches a heightmap to return shadow…|I:Texture Object,UVs,Light Vector WorldSpace,Max Steps,Shadow Density,Start Bias,Height Scale,Trace Distance,SubUV Frames,Animation Phase,Temporal Jitter,Heightmap Channel|O:Light Energy,Raw Heightmap Value,Step Complexity
F|DistanceField_Capsule|Draws a line between 2 points using supplied 3D coordin…|I:Coordinates,P0,P1,Width|O:*
F|DistanceField_Cylinder|Generates a distance field shape for a capped cylinder.|I:Coordinates,Center,h|O:*
F|DistanceField_Intersection|Returns the intersection of two distance field function…|I:Distance Field 1,Distance Field 2|O:*
F|DistanceField_Sphere|Draws a line between 2 points using supplied 3D coordin…|I:Coordinates,Center,Radius|O:*
F|DistanceField_Subtract|Subtracts Distance Field 2 from Distance Field 1|I:Distance Field 1,Distance Field 2|O:*
F|DistanceField_Union|Returns the Union of two distance field shapes.|I:Distance Field 1,Distance Field 2|O:*
F|RayTraceSphereFalloff|finds the distance to the sphere|I:Sphere Radius,Sphere Falloff,Unit Ray Direction,Sphere Center,Ray Origin|O:Clamped Falloff,Unclamped Results
F|Parallax_For_Bomb|Parallax Occlusion Mapping uses Ray Tracing to find the…|I:Heightmap Texture,Height Ratio,Min Steps,Max Steps,UVs,Heightmap Channel,Reference Plane,-----------------------------,Specify Manual Texture Size,Manual Texture Size,Override Camera Vector,------------------------------,Render Shadows (Occlusion Mapping),Light Vector,Shadow Steps,Shadow Penumbra|O:Parallax UVs,Offset Only,Shadow,Pixel Depth Offset,World Position,Tangent Light Vector,Material Complexity - Steps Debug
F|TextureBomb_SingleSample|-|I:Cell Index,UVs,Offset Strength,TexObject,IsNormal?|O:UVs,Tangent Space Camera Vector,Texture Sample,Normal Flip
F|TextureBomb_SingleSample_POM|-|I:Cell Index,UVs,Offset Strength,TexObject,IsNormal?,HeightTex,HeightRatio|O:UVs,Texture Sample
F|TreeAnimationSines|Add time and a gradient to create an animation used for…|I:Time and Grad,LS1,LS2,LS3,LS4|O:*
F|PivotPainter2FoliageAnimation|-|I:Enable,Enable Normal Rotation,Pivot Painter Texture Coordinate,Motion Dampening Falloff Radius,Optional - world space pixel normal,Texture Dimensions To Gather Parent UVs,Wind Gust Angle Rotation,Wind Gust Offset,Wind Speed Down Wind Vector,Layer Mask,Advanced - Parent Rotation Angle Influence,Wind Shelter Settings,Random Rotation Texture Sample Scale,Random Rotation Influence,Position And Index Texture,Wind Direction,Wind Direction Y Axis,Wind Gust World Scale,X-axis and X-Extent Texture,Wind Speed Horizontal Speed,Optional - Wind Turbulence and Gust Mag,Use Wind Shelter Settings|O:Parent Index Integer,Parent UVs,World Position Offset,Final World Position,Rotated World Space Pixel Normal,Advanced - Rotation Angle Animation
F|ColorCorrection|Color correction|I:Brightness,Color,Contrast,Gain,Gamma,Hue Shift,Lift,Saturation|O:*
F|Contrast_Preserve_Color|This function allows you to modify the contrast of an i…|I:Color,Contrast|O:*
F|HighPassFunction|Performs a high pass type operation on the input functi…|I:Position,Contrast,Highpass Offset,Center Sample,Offset Sample +X,Offset Sample -X,Offset Sample +Y,Offset Sample -Y,Offset Sample +Z,Offset Sample -Z,Number of Samples|O:Result,Offset +X,Offset -X,Offset +Y,Offset -Y,Offset +Z,Offset -Z
F|HighPassTexture|Performs a high pass type operation on an input texture…|I:Texture Object,UVs,Contrast,Highpass Offset,High Quality|O:Result No Contrast,Result
F|Luminosity_And_Color|This function takes an input color and an input luminos…|I:Color,Luminosity|O:*
F|UnSharpMaskFunction|Performs a high pass type operation on the input functi…|I:Position,Amount,Sample Offset,Center Sample,Offset Sample +X,Offset Sample -X,Offset Sample +Y,Offset Sample -Y,Offset Sample +Z,Offset Sample -Z,Number of Samples|O:Result,Offset +X,Offset -X,Offset +Y,Offset -Y,Offset +Z,Offset -Z
F|UnSharpMaskTexture|Performs a high pass type operation on an input texture…|I:Texture Object,UVs,Amount,Sample Offset,High Quality,TextureSize|O:*
F|Landscape_Manual_UVW|Landscape Manual UVW Defined by Min and Max positions|I:Min Pos,Max Pos,Position|O:*
F|GGXSpecular|Returns a specular lobe using GGX.|I:Normal,Light Vector,Roughness|O:*
F|ThresholdWithRange|-|I:ThresholdValue,ThresholdRange,Alpha,TwoSidedThreshold|O:*
F|2dArrayLookupByIndex|Finds an index's location in a 2d Array.|I:Array Dimensions,Index|O:*
F|AngleBetweenVectors|Find the angle between two normalized vectors in degree…|I:Normalized V1,Normalized V2|O:Angle In Degrees,0-1
F|ArrangePointsEvenlyAroundABox|This material function will evenly arrange points aroun…|I:X Vector,Y Vector,Z Vector,Position,Relative Pivot Location,XY Phase (0-1),Z Phase (0-1)|O:Point Around Box,World normal
F|CylinderIntersection|Returns an analytical intersection for a cylinder of th…|I:Origin,Radius,Z Axis,X Axis,XY Scale,Capped?,Z Min-Max|O:Ray Entry Position,Ray Exit Position,Cylinder Thickness,Opacity Mask,Normal,T0,T1
F|DegreesToRadians|Converts from Degrees to Radians.|I:*|O:*
F|FindSaturation|Finds the saturation of a color.|I:*|O:*
F|ProjectVectorOntoPlane|Projects a vector onto a plane by removing it's deviati…|I:Plane Normal,Vector|O:*
F|QuadraticFormula|Solved a quadratic equation of the form ax^2 + bx + c =…|I:A,B,C|O:T0,T1,Discriminant
F|RadiansToDegrees|Converts from Radians to Degrees.|I:*|O:*
F|RemapValueRange|Generalized remapping function to explicitly remap an i…|I:Input,Input Low,Input High,Target Low,Target High|O:*
F|RemapValueRangeNormalized|Generalized remapping function to explicitly remap an i…|I:Input,Input Low,Input High|O:*
F|SmoothCeil|Smooth ceil is like ceil but gives a smooth ramp before…|I:In,Ramp Width|O:*
F|WrapFloat|Similar to fmod with support for negative floats : retu…|I:Value,Wrap|O:*
F|WrapFloat2|Similar to fmod with support for negative floats : retu…|I:Value,Wrap|O:*
F|WrapFloat3|Similar to fmod with support for negative floats : retu…|I:Value,Wrap|O:*
F|WrapFloat4|Similar to fmod with support for negative floats : retu…|I:Value,Wrap|O:*
F|ms_StaticMeshSkeletalAnimation|This material function decodes the skeletal mesh animat…|I:Animation Phase,Rest Pose Texture,Position Animation,Rotation Animation,World Space Normals,Vertex Shader Bone Index,Pixel Shader Bone Index,World Position|O:World Position Offset,World Space Normals,Advanced: Mesh Rotation Axis And Angle
F|ms_StaticMeshSkeletalAnimationHighQuality|This material function decodes the skeletal mesh animat…|I:Animation Phase,Rest Pose Texture,Position Animation,Rotation Animation,Tangent Space Normal Map,Vertex Shader Bone Index,Tangent Basis X In WS,Tangent Basis Y In WS,Tangent Basis Z In WS,World Position|O:World Position Offset,World Space Normals,Custom UV 2,Custom UV 3,Custom UV 4,Custom UV 5,Custom UV 6,Updated Vertex Shader X Vector,Updated Vertex Shader Y Vector,Updated Vertex Shader Z Vector,Updated Pixel Shader X Vector,Updated Pixel Shader Y Vector,Updated Pixel Shader Z Vector
F|MS_VertexAnimationTools_MorphTargets|This material function will apply the VertexAnimationTo…|I:Morph Animation,Morph Normal,Morph Texture,Number of Morph Targets,0-1 Animation Value?,Morph Target UV|O:Pixel Shader World Vertex Normal (See tooltip),Pixel Shader Tangent Vertex Normal (See tooltip),World Position Offset,Custom UV 2 (Needed),Custom UV 3 (Needed),Vert shader Normal (Advanced)
F|AlignFacingParticlesByVelocity2D|-|I:-|O:*
F|AlphaOffset|Applies an offset to alpha while keeping the range 0 to…|I:Alpha,Offset|O:*
F|BakedDisplacement|Set up a baked scalar displacement map to be used with…|I:In,Baked_Min,Baked_Max|O:*
F|BellCurve|Gives a Bell Curve also known as a Normal Distribution|I:*|O:0-1,Standard
F|BoxIntersection|Returns Entry and Exit points for a Ray intersecting an…|I:Ray Origin,Ray Direction,Box Min,Box Max|O:Ray Entry Position,Ray Exit Position,Box Thickness,T0,T1
F|BreakOutFloat2Components|Enter a float 2 vector into the function and retrieve i…|I:*|O:R,G
F|BreakOutFloat3Components|Enter a float 3 vector into the function and retrieve i…|I:*|O:R,G,B
F|BreakOutFloat4Components|Enter a float 4 vector into the function and retrieve i…|I:*|O:R,G,B,A
F|CameraDepthFade|Creates a gradient of 0 near the camera to white at Fad…|I:Fade Length,Fade Offset,For Vertex Shader|O:*
F|ComponentBasisVectors@/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/ComponentBasisVectors.ComponentBasisVectors|The local XYZ component transform vectors in world spac…|I:-|O:X,Y,Z
F|ComponentBasisVectors@/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/V2/ComponentBasisVectors.ComponentBasisVectors|The local XYZ component transform vectors in world spac…|I:-|O:X,Y,Z
F|ComponentPivotLocation|Returns the world position of the components origin.|I:-|O:*
F|ComponentWise_SphereMask|Apply a sphere mask for each channel of a vector indepe…|I:A,B,Radius,Hardness|O:*
F|Compute3DDeriv|Uses positions offset in a tetrahedral pattern to compu…|I:Value1,Value2,Value3,Value4,Tetrahedral Offset|O:dx,dy,dz,Value
F|ComputeFilterWidth|-|I:*|O:*
F|ComputeMipLevel|-|I:Texture Size,UVs|O:*
F|ConvertFromDiffSpec|-|I:DiffuseColor,SpecularColor|O:BaseColor,Metallic,Specular
F|CorrectPixelDepthOffsetValue|Extends pdo distance as the camera aligns with the surf…|I:*|O:*
F|CurlFrom3DDeriv|Compute curl of at 3D vector field from result of Prepa…|I:dx,dy,dz|O:*
F|DeriveTangentBasis|Derive a secondary tangent basis from another UV channe…|I:UVs,Normal|O:Tangent,Binormal,World Space Normal
F|DespillByHue|-|I:Texture,Despill Hue,Hue Range,DeSpill Amount|O:*
F|DiffColorKeyer|-|I:GreenScreen,KeyColor,AlphaThresOffset,WeightsRB,ClipBW,UnPremult|O:*
F|DitherTemporalAA|Stipple pattern/Dither in screen space and time to work…|I:Alpha Threshold,Random|O:*
F|DrawLine-2D|Draws a line between 2 points using supplied 2D coordin…|I:Coordinates,P0,P1,Line Width,Edge Falloff,Square Corners?|O:*
F|DrawLine-3D|Draws a line between 2 points using supplied 3D coordin…|I:Coordinates,P0,P1,Line Width,Edge Falloff,Square Corners?|O:*
F|DynamicBranch|The code connected to the "Color Input 1" will be execu…|I:Alpha,Color Input 0,Color Input 1|O:*
F|DynamicNormalFromDistanceField|Generate animated normals from offset distance fields u…|I:Right Shifted Distance Field,Downward Shifted Distance Field,Unshifted distance field,Dissolve Alpha,Normal Lip Curvature,Normal Lip Tightness|O:Mask,Normal,Normal XY (Advanced),Thresholded Gradients (Advanced)
F|ExponentialDensity|Uses the D3DFOG_EXP function to map exponential density.|I:Depth,Density,Use Exp2|O:*
F|FlipBook|Animates a texture in a flipbook like fashion.|I:Animation  Phase (0-1),Number of Columns,Number of Rows,Texture,UVs,MipBias/Level,Clamp Anim (see tooltip),Use Mip Bias (T) Level (F)|O:Result,Alpha,UVs,UV Center
F|FlipBook_MotionVectors|Flipbook with additional options for Motion Vectors.|I:Animation  Phase (0-1),Number of Columns X,Number of Rows Y,Texture,UVs,Motion Vector Texture,Motion Vector Intensity,Phase to Debug,Double Apply Motion Vectors,Custom UV Input,Custom UV2 Input,Use Custom UVs|O:Result,Alpha,Blend Phase,Forward Motion Vectors,CustomUV Output,CustomUV2 Output
F|FlipBook_UniformNonUniform|This is a special version of the flipbook function only…|I:Animation  Phase (0-1),Number of Columns,Number of Rows,Texture,UVs,Clamp Anim (see tooltip),MipBias|O:Result,UVs,Y Row,Alpha,Blend Phase
F|FoliageScaleFactor|A way to get object scale for Foliage meshes where easi…|I:*|O:*
F|FOV|Returns the current cameras FOV setting|I:-|O:FOV ,FOV in radians,FOV angle in degrees
F|FunctionGraphSetup|-|I:Gradient Height,X range Y range,UVs|O:Range,UV,Corrected Y,Gradient Height,x,y
F|GradFrom3DDeriv|Compute 3D gradient vector from result of Prepare3DDeri…|I:dx,dy,dz|O:*
F|Henyey-Greenstein-Phase|-|I:Anisotropy,AngleDegrees,Light Vector|O:*
F|IsFloatValid|Returns 1 if the float is a real number and 0 if it is…|I:*|O:*
F|Lerp_3Color|Lerps 3 inputs based on a single value.|I:A,B,C,Alpha|O:*
F|Lerp_Multiple_Float|Lerps multiple inputs based on a single value.|I:1,2,3,4,A|O:Lerp 3 Inputs,Lerp 4 Inputs
F|Lerp_Multiple_Float2|Lerps multiple inputs based on a single value.|I:1,2,3,4,A|O:Lerp 3 Inputs,Lerp 4 Inputs
F|Lerp_Multiple_Float3|Lerps multiple inputs based on a single value.|I:1,2,3,4,A|O:Lerp 3 Inputs,Lerp 4 Inputs
F|Lerp_Multiple_Float4|Lerps multiple inputs based on a single value.|I:1,2,3,4,A|O:Lerp 3 Inputs,Lerp 4 Inputs
F|LumensFromLightSource|Returns the per pixel brightness of a spherical light a…|I:Light Color,Light Radius,Light Source Lumens|O:*
F|MacroUVs|-|I:-|O:-
F|MakeFloat2|Creates a float 2 vector from a series of scalar inputs.|I:X,Y|O:*
F|MakeFloat3|Creates a float 3 vector from a series of scalar inputs.|I:X,Y,Z|O:*
F|MakeFloat4|Creates a float 4 vector from a series of scalar inputs.|I:X,Y,Z,A|O:*
F|MatLayerBlend_BreakOpacity|-|I:*|O:*
F|MF_OrthoHeight|-|I:*|O:*
F|MF_OrthoWidth|-|I:*|O:*
F|MF_RotateVector_90|Rotates vectors along any cardinal axis (Right hand coo…|I:*|O:CW X,CCW X,CW Y,CCW Y,CW Z,CCW Z
F|MF_SchlickApprox|-|I:*|O:*
F|MF_SchlickApprox1|-|I:*|O:*
F|MF_SchlickInternal|-|I:In_IOR,Out_IOR|O:*
F|MF_SchlickInternal1|-|I:In_IOR,Out_IOR|O:*
F|MF_SmoothMax|-|I:A,B,distance|O:*
F|MF_SmoothMax1|-|I:A,B,distance|O:*
F|MF_SmoothMin|-|I:A,B,distance|O:*
F|MF_SmoothMin1|-|I:A,B,distance|O:*
F|MF_TransmittanceToMeanFreePath|Compute extinction coefficient and convert to mean free…|I:TransmissionColor,TransmissionDepth,TransmissionScatter|O:*
F|ML_ExampleMaterialLayer|-|I:Tiling,Tint|O:*
F|ms_PivotPainter2_SampleLayerData|-|I:Current Index (ParentUVs),UVs,Texture resolution (ParentUVs)|O:Position and Parent Index,X axis vector and X extent,Parent Index,Parent UVs,Is Child?
F|MulM4V4|-|I:MatrixRow1,MatrixRow2,MatrixRow3,MatrixRow4,Vector|O:*
F|MultiplyVectorWithQuaternion|-|I:Vector,Quat,Invert Quaternion|O:*
F|ObjectLocalBounds|-|I:-|O:Local Bounds Minimum,Local Bounds Max,Local Bounds Size
F|ObjectLocalToWorldData|Returns object level information.|I:*|O:Object Pivot Location,Object Scale,Object Scale XYZ,World Vector
F|OffsetAndScaleTo1|The value entered in the original value input is offset…|I:Original Value,Offset Amount|O:*
F|PackTwoNormalizedFloats|Packs two normalized floats (0-1) onto one single float.|I:NormalizedFloatA,NormalizedFloatB|O:*
F|ParticleDOF|Use with with CircleDOF|I:*|O:Opacity,WorldPositionOffset
F|PassThrough|This node simply passes any inserted values through its…|I:S,V2,V3,V4|O:S,V2,V3,V4
F|PerturbNormalHQ|-|I:Bump one pixel right,Bump center,Bump one pixel down,WS Normal|O:*
F|PerturbNormalLQ|-|I:*|O:*
F|PixelInWorldUnits|-|I:Depth,Pixel|O:*
F|PlotFunctionOnGraph|Plots f(x) = y to visualize the output of another funct…|I:Gradient Height,X range Y range,ShowGrid?,Thickness,Color,f(x)|O:f(x) = y,x
F|PlotFunctionOnGraph_Derivative|Plots f(x) = y to visualize the output of another funct…|I:Gradient Height,X range Y range,ShowGrid?,Thickness,Color,f(x),f(x + Δx)|O:d(x),f(x) = y,x,x + Δx
F|PlotFunctionOnGraph_Setup_Input|Plots f(x) = y to visualize the output of another funct…|I:X range Y range,UVs,Corrected Y-size,Gradient Height,Thickness,Color,ShowGrid?,f(x)|O:*
F|PointSampledUVs|Returns UVs that are point sampled which is a way to fo…|I:UVs,Texture Size|O:*
F|Posterize|-|I:Diffuse,Number of value steps|O:*
F|PowerToRoughness|-|I:*|O:*
F|Prepare3DDeriv|Uses positions offset in a tetrahedral pattern to compu…|I:Position,Tetrahedral Offset|O:Offset1,Offset2,Offset3,Offset4
F|PreparePerturbNormalHQ|-|I:*|O:Value one pixel right,Value,Value one pixel down,FilterWidth
F|ProtectFrom0|-|I:*|O:RGB,R,G,B
F|pythagoreanTheorum|-|I:*|O:*
F|QuatAxisAngleConversions|Convert a quat to an angle axis and vice versa.|I:AxisAngle,Quaternion|O:Axis Angle As Quat,Quat as Axis Angle
F|Refract@/Engine/Functions/Engine_MaterialFunctions01/Vectors/Refract.Refract|Calculates vector based Refraction using the hlsl intri…|I:Ray Direction,Surface Normal,Refractive Index Origin,Refractive Index Target|O:*
F|Refract@/Engine/Functions/Engine_MaterialFunctions02/Math/Refract.Refract|-|I:IncidenceVector,Normal,RatioOfIndicesOfRefraction|O:*
F|RGBtoHSV@/Engine/Functions/Engine_MaterialFunctions01/Chromakeying/RGBtoHSV.RGBtoHSV|-|I:*|O:*
F|ScaleUVsAroundPoint|-|I:Offset XY Texturesize Z,Texture Scale,UVs|O:UVs,0-1 mask
F|ScaleUVsByCenter|-|I:Texture Scale,UVs|O:UVs,0-1 mask
F|SceneTextureAverage|Samples and averages the scene texture 8 times in a cir…|I:*|O:*
F|SchlickPhase|The Schlick Phase Function is useful for adding some di…|I:Cosine,Anisotropy|O:*
F|SmoothStep|HLSL smoothstep function.|I:Alpha,Min,Max|O:*
F|SphereGradient-2D|Generates a gradient representing the depth of a shere…|I:UVs,CenterPosition,Radius|O:Result 0-1,Result Diameter,Result Radius
F|SphereGradient-3D|Generates a gradient representing the depth of a shere…|I:Location,Offset,Radius,Calculate Camera Inside,Depth Biased Alpha,FadeDistance|O:Result 0-1,Result Diameter,Result Radius
F|SplitComponents|-|I:*|O:RGB,R,G,B
F|StencilMaskCompare|Compares a float to the stencil buffer.|I:*|O:*
F|Step|-|I:High,Low|O:*
F|Swizzle|-|I:XY,XYZ|O:YX,YXZ
F|TangentBasis|Retrieves the tangent basis in world space|I:-|O:X U,Y V,Z W
F|TextureVariation_RotateNormals|-|I:Vector,Normal|O:*
F|TextureVariation_RotateUV|-|I:UVs,Offset,Vector|O:*
F|TimeWithSpeedVariable|Time multiplied by speed with an option to use the rema…|I:Speed,Time|O:Frac Time,Time
F|TransformNormals_Tangent_to_Vertex|Useful for when you want a World Aligned texture to pic…|I:Vector to Transform,Squash Vertex Normals|O:*
F|TransformToZVector|This transforms a vector based on a Z vector and genera…|I:Vector to Transform,Z Vector,Center Location|O:*
F|UnpackTwoNormalizedFloats|Unpacks a float value encoded by the function PackTwoNo…|I:*|O:NormalizedFloatA,NormalizedFloatB
F|VectorLength|Returns a vectors length.|I:Vector 3,Vector 2|O:V3 Length,V2 Length
F|WithinRange|Returns 1 if a value is within the provided range limit…|I:RangeMin,RangeMax,Value|O:*
F|WithinRangeFloat2|Returns 1 if a value is within the provided range limit…|I:RangeMin,RangeMax,Value|O:AllComponentsWithinRange,AnyComponentsWithinRange
F|WithinRangeFloat3|Returns 1 if a value is within the provided range limit…|I:RangeMin,RangeMax,Value|O:AllComponentsWithinRange,AnyComponentsWithinRange
F|WithinRangeFloat4|Returns 1 if a value is within the provided range limit…|I:RangeMin,RangeMax,Value|O:AllComponentsWithinRange,AnyComponentsWithinRange
F|WorldAlignedBlend|-|I:In Explicit Normal,In World Vector,Blend Sharpness,Blend Bias,Clamped?,Alpha|O:Alpha,w/ Explicit Normal,w/Vertex Normals
F|WorldPosition-XY|WorldPosition XY Coordinates with Scale input.|I:*|O:*
F|WorldUnitsInPixel|-|I:Depth,WorldUnits|O:*
F|Blend_ColorBurn|The darker the Blend texture, the more color in the fin…|I:Base,Blend|O:*
F|Blend_ColorDodge|Divides the Base texture by the inverted Blend texture.|I:Base,Blend|O:*
F|Blend_Darken|Returns the darker of the two values for each pixel.|I:Base,Blend|O:*
F|Blend_Difference|Subtracts the Blend from the Base, Abs the results to e…|I:Base,Blend|O:*
F|Blend_Exclusion|Halves the Blend and Base, combines them together, then…|I:Base,Blend|O:*
F|Blend_HardLight|Harsher version of Soft Light blend|I:Base,Blend|O:*
F|Blend_Lighten|Returns the lighter of the two values for each pixel.|I:Base,Blend|O:*
F|Blend_LinearBurn|Adds the two textures then subtracts one from the result|I:Base,Blend|O:*
F|Blend_LinearDodge|Adds the base and blend together.|I:Base,Blend|O:*
F|Blend_LinearLight|Linear version of Overlay blend mode, harsh results.|I:Base,Blend|O:*
F|Blend_Overlay|Emulates Photoshop's overlay blend mode.|I:Base,Blend|O:*
F|Blend_PinLight|Softer version of Overlay, solid white or black as blen…|I:Base,Blend|O:*
F|Blend_Screen|Inverts each texture, multiplies them together, then re…|I:Base,Blend|O:*
F|Blend_SoftLight|Softer version of Overlay, solid white or black as blen…|I:Base,Blend|O:*
F|Lerp_ScratchGrime|Use to creat Material layers that have scratches and gr…|I:Base,ScratchValue,GrimeValue,ScratchMask,GrimeMask|O:*
F|Lerp_ScratchGrime2|Use to creat Material layers that have scratches and gr…|I:Base,ScratchValue,GrimeValue,ScratchMask,GrimeMask|O:*
F|Motion_4WayChaos|4-way diagonal motion|I:Coordinates,Divisor,Speed,Texture|O:*
F|Motion_4WayChaos_Normal|4-way diagonal motion, normal maps only|I:Coordinates,Divisor,Speed,Texture|O:*
F|BlurSampleOffsets|Multiplies an input offset by a number of 2d vectors.|I:*|O:0,1,1,0,0,-1,-1,0,-.5,.5,.5,.5,.5,-.5,-.5,-.5
F|BoundingBoxBased_0-1_UVW|Creates a locally aligned 0-1 value on XY and Z.|I:-|O:RGB,R,G,B
F|LocalPosition|-|I:-|O:Local Position,Instance Local Position,Local Position (Excluding Offsets),Instance Local Position (Excluding Offsets)
F|PanTextureCoordinateChannelfrom-1ton+1|This function pans a 0-1 texture coordinate channel fro…|I:UV Channel,Tiling Amount,Time (0-1)|O:*
F|PanTextureCoordinateFrom-1toN+1|This function pans 0-1 uv coordinates from -1 to the nu…|I:UVs,UV Tiling,Time (0-1)|O:*
F|SampleSceneDepth|Samples the scene depth texture using multiple methods.|I:Fraction Offset,Pixel Offset,Use Custom Depth|O:Depth Using Fraction Offset,Depth Using Pixel Offset
F|ScreenResolution|Retrieves the visible screen resolution and the render…|I:-|O:Visible Resolution,Buffer Resolution
F|UVBrickPatterns|Takes coordinates and manipulates thems to form an offs…|I:Float 2 Coordinates,Offset Percentage,Offset X (True) Or Offset Y (False)|O:Frac,Non-frac
F|UVRemap_0-1_ToRange|Remaps UVs from 0-1 to the specified range.|I:X range Y range,UVs|O:Range,UV,x,y
F|VirtualPlaneCoordinates|Virtual coordinates for a raytraced plane, in world uni…|I:Plane Normal Axis,Plane X Axis,Plane Center,UV Scale|O:UVs,World Position,World Position - Centered
F|LongLatToUV|This node transforms a directional vector into a UV val…|I:*|O:*
F|UVToLongLat|This node transforms a UV value into a directional vect…|I:*|O:*
F|DebugFloat2Values|Plug a vector into the function and then preview the ou…|I:Vector2,MaximumNumberOfDigits,UVs,DebugTextLocation RG_UpperRight BA_LowerLeft,Component Spacing|O:ColorCodedOutput,GreyScaleOutput
F|DebugFloat3Values|Plug a vector into the function and then preview the ou…|I:Vector3,MaximumNumberOfDigits,UVs,DebugTextLocation RG_UpperRight BA_LowerLeft,Component Spacing|O:ColorCodedOutput,GreyScaleOutput
F|DebugFloat4Values|Plug a vector into the function and then preview the ou…|I:Vector4,MaximumNumberOfDigits,UVs,DebugTextLocation RG_UpperRight BA_LowerLeft,Component Spacing|O:ColorCodedOutput,GreyScaleOutput
F|DebugIntValues|Enter a value into the material function and read its r…|I:Number,MaximumNumberOfDigits,DebugTextLocation RG_UpperRight BA_LowerLeft,UVs|O:*
F|DebugOnOff|Useful for doing AB comparrison in material|I:-|O:*
F|DebugScalarValues|Enter a value into the material function and read its r…|I:Number,MaximumNumberOfDigits,UVs,DebugTextLocation RG_UpperRight BA_LowerLeft|O:*
F|DebugTimeSine|useful for seeing what a scalar value does between 0 an…|I:*|O:*
F|DepthFromWorldPosition|Returns the same value that Pixel Depth or Scene Depth…|I:*|O:*
F|PixelDepthOffset_Foliage|This function helps set up PixelDepthOffset for foliage…|I:WorldPositionOffset,Dynamic Shadow Distance,Dynamic Shadow Fade Length,Initial Radius,CustomUV Input,Depth Texture|O:World Position Offset,Custom UVs,Pixel Depth Offset
F|GetAmbientCubemapIntensity|Get Ambient Cubemap Intensity|I:-|O:*
F|GetAmbientCubemapTint|Get Ambient Cubemap Tint|I:-|O:*
F|DiamondGradient|Uses UV Channel 0 to generate a Diamond Gradient|I:*|O:*
F|GetGradientMapRow|Gets the row needed for a given gradient index in a gra…|I:Atlas Height,CurveTime,Index (0 Based)|O:*
F|GradientMap_Multi|Maps a 0-1 value to a color gradient slice.|I:Gradient Texture,Greyscale Value To Gradient Map,Index (0 Based),Number Of Gradients In the Gradient Map|O:RGB,A
F|GradientMap_Multi_TexObjSamplerType|Maps a 0-1 value to a color gradient slice.|I:Gradient Texture,Greyscale Value To Gradient Map,Index (0 Based),Number Of Gradients In the Gradient Map|O:RGB,A
F|LinearGradient|Uses UV Channel 0 to generate a linear gradient along t…|I:*|O:UGradient,VGradient
F|RadialGradient|Uses UV Channel 0 to create a radial gradient|I:CenterPosition,Radius|O:*
F|RadialGradientExponential|Creates a radial gradient using the input UV coordinate…|I:UVs,CenterPosition,Radius,Density,Invert Density|O:*
F|SmoothCurve|Adjust the tangents at x0 and x1 to adjust x's curve.|I:X,Tangent 0,Tangent 1|O:*
F|ValueStep|Takes a gradient with values over one and masks out a p…|I:Gradient,Mask Offset Value,Number Before White Result|O:*
F|3ColorBlend|Blends between 3 colors based on a greyscale input|I:A,B,C,Alpha|O:*
F|3PointLevels|Remaps 0-1 values by linearly interpolating through 3 n…|I:Texture,---------------,New Black Value,New Middle Value,New White Value,Middle Point,--------------- ,Define Interpolation Curve,Interpolation Power,Invert Interpolation Power|O:*
F|CheapContrast|Cheaply adds contrast similar to pulling in edges in Ph…|I:In,Contrast|O:*
F|CheapContrast_RGB|Cheaply adds contrast similar to pulling in edges in Ph…|I:In,Contrast|O:*
F|DeriveHDRfromLDR|Derive an HDR range from an LDR texture while maintaini…|I:LDR Input,HDR Dynamic Range,HDR Intensity Multiplier,HDR Tint,Derive HDR Power,Derive Luminance from Linear,Desaturate Luminance|O:*
F|HueShift|Adjusts the hue of an image.|I:Hue Shift Percentage,Texture|O:*
F|RaiseBlackLevelsByPercentage|Raises the black levels of an input value based on a pe…|I:Image,Black intensity level|O:*
F|SCurve|Applies an S curve image adjustment|I:In,Power|O:*
F|SmoothThreshold|Smooth contrast applied after a threshold value is pass…|I:Cutoff Value,Gradient,Lerp Value|O:*
F|CheckOcclusion|Checks to see if a world position is occluded by an opa…|I:Position To check for Occlusion,Depth Occlusion Falloff,Offscreen Falloff Range|O:Screen Edge And Occlusion,Occlusion,Screen Edge
F|MatLayerBlend_AddWorldPositionOffset|Adds WorldPositionOffset|I:Material,WorldPositionOffset|O:*
F|MatLayerBlend_AO|Blends an AO map to remove reflection.|I:Material,AO|O:*
F|MatLayerBlend_BakedNormal|Blends a Processed Normal Map with layered normals|I:Material,Normal|O:*
F|MatLayerBlend_BakedNormal_SimpleAdd|Blends a Processed Normal Map with layered normals|I:Material,Normal|O:*
F|MatLayerBlend_BlendAngleCorrectedNormals|Replaces WorldPositionDisplacement|I:Material,Additional Normal,Mask|O:*
F|MatLayerBlend_BreakBaseColor|Replace the Base Color|I:*|O:*
F|MatLayerBlend_BreakNormal|Break out the Normal|I:*|O:*
F|MatLayerBlend_Decal|Blends in a decal sheet using the 2nd uv channel|I:Base Material,DecalNormalFlatness,DecalRoughness,DecalSheet|O:*
F|MatLayerBlend_Decal_UV3|Blends in a decal sheet using the 2nd uv channel|I:Base Material,DecalNormalFlatness,DecalRoughness,DecalSheet|O:*
F|MatLayerBlend_Displacement|Adds Displacement|I:Material,Displacement,Tessellation Multiplier|O:*
F|MatLayerBlend_Emissive|Adds Emissive|I:Material,Emissive|O:*
F|MatLayerBlend_LightmassReplace|Replace the Base Color in Lightmass|I:Material,LightmassReplaceColor|O:*
F|MatLayerBlend_ModulateRoughness|Modulates the roughness value, useful for greasy look.|I:Base Material,RoughnessMultiplier|O:*
F|MatLayerBlend_ModulateSpecular|Modulates the Specular value|I:Base Material,SpecularMultiplier|O:*
F|MatLayerBlend_Multiply|Multiplies all elements of Material Attributes by Multi…|I:Base Material,Multiplier|O:*
F|MatLayerBlend_MultiplyBaseColor|Multiply the Base Color by a Color|I:Material,NewBaseColor,Mask|O:*
F|MatLayerBlend_NormalBlend|Blends a Normalmap on top of a material using a mask.|I:Material,NormalMask,Normal|O:*
F|MatLayerBlend_NormalFlatten|Diminishes the effect of a normalmap.|I:Material,NormalFlatness,Normal|O:*
F|MatLayerBlend_OverrideBaseColor|Replace the Base Color|I:Material,NewBaseColor,Mask|O:*
F|MatLayerBlend_OverrideDisplacement|Replaces WorldPositionDisplacement|I:Material,WorldPositionDisplacement,Mask,TessellationMultiplier|O:*
F|MatLayerBlend_OverrideMetalness|Replace the Metalness|I:Material,NewMetalness,Mask|O:*
F|MatLayerBlend_OverrideOpacity|Replaced the Opacity|I:Material,NewOpacity,Mask|O:*
F|MatLayerBlend_OverrideOpacityMask|Replaced the Opacity Mask|I:Material,NewOpacityMask,Mask|O:*
F|MatLayerBlend_OverrideSubSurface|Replace the Subsurface Color and Opacity|I:Material,NewOpacity,NewSubSurfaceColor,Mask|O:*
F|MatLayerBlend_OverrideWorldPositionOffset|Replaces WorldPositionOffset|I:Material,Mask,WorldPositionOffset|O:*
F|MatLayerBlend_ReplaceNormals|-|I:Material,Normal|O:*
F|MatLayerBlend_RoughnessOverride|Replace the Roughness|I:Material,NewRoughness,Mask|O:*
F|MatLayerBlend_SeparateNormalandColorClamps|Blends all attributes of 2 Materials|I:Base Material,Top Material,Alpha,Color Blend Min,Color Blend Max,Normal Blend Min,Normal Blend Max|O:Blended Material,Displacement
F|MatLayerBlend_Simple|Blends all attributes of 2 Materials except Normal.|I:Base Material,Top Material,Alpha|O:*
F|MatLayerBlend_Stain|Blends the top layer as a stain, only the color and rou…|I:Base Material,Top Material,Alpha,StainPremultiply|O:*
F|MatLayerBlend_Standard|Blends all attributes of 2 Materials|I:Base Material,Top Material,Alpha|O:*
F|MatLayerBlend_StandardWithDisplacement|Blends all attributes of 2 Materials|I:Base Material,Top Material,Alpha|O:Blended Material,Displacement
F|MatLayerBlend_StandardWithMaskEdgeTint|Blends all attributes of 2 Materials|I:Base Material,Top Material,Alpha,Tint Mask|O:Blended Material,Displacement
F|MatLayerBlend_TenLayerBlend|Fixed function blending of 10 layers.|I:Layer10,Layer10_Mask,Layer9,Layer9_Mask,Layer8,Layer8_Mask
,Layer7,Layer7_Mask,Layer6,Layer6_Mask
,Layer5,Layer5_Mask,Layer4,Layer4_Mask,Layer3,Layer3_Mask,Layer2,Layer2_Mask,Layer1,Layer1_Mask,Background,<BakedNormal>|O:*
F|MatLayerBlend_Tint|Simple Tinting of Base Color|I:Material,Tint,TintMask|O:*
F|MatLayerBlend_TintAllChannels|Simple Tinting of Base Color|I:Material,Tint,TintMask|O:*
F|MatLayerBlend_TopNormal|Blends Material Attributes but only uses the Top Normal…|I:Base Material,Top Material,Alpha|O:*
F|AddComponents|Input a float 2, 3 or 4 and retrieve the sum of the com…|I:f2,f3,f4|O:f2,f3,f4
F|ConcatenateMatrices|Concatenate 2 matrices|I:BasisX,BasisY,BasisZ,BasisW,----------,BasisX2,BasisY2,BasisZ2,BasisW2|O:X,Y,Z,W
F|CreateThirdOrthogonalVector|Takes two vectors and generates a third orthogonal vect…|I:Vector1,Vector2|O:Vector1,Vector2,Vector3
F|DeleteReference4x4Matrix|Transform a vector into a new basis|I:VectorToTransform,BasisX,BasisY,BasisZ,BasisPosition|O:*
F|DeriveNormalZ_Function|DeriveNormalZ expanded into a material function, includ…|I:XY vector,Z sign,Default Normalization vector|O:*
F|InverseTransformMatrix|Transform a vector into a new basis|I:VectorToTransform,BasisX,BasisY,BasisZ|O:*
F|LinearSine|A sine-like function that transitions linearly in the 0…|I:Value,Period,-1 to 1,Sine Phase|O:Linear Sine,Rounded Linear Sine ,Direction
F|LineIntervalIntersection|Returns the point of intersection for two lines.|I:Line1 - A.y,Line1 - B.y,Line2 - A.y,Line2 - B.y,A.x,B.x|O:xy,x,y
F|MakeVectorsOrthogonal|Makes vectors orthagonal by using the cross product of…|I:Vector1,Vector2,Vector3|O:Vector1,Vector2,Vector3
F|MultiplyAdd|Modulate the "add" input by by the base input and then…|I:Base,Add|O:*
F|Pi|Pi multiplied by an input value.|I:*|O:*
F|RayTracedSphere|-|I:Sphere Position,Sphere Radius,RayDirection,World position|O:Ray Intersection Position ,Intersection Surface Normal,Ray Hit Bool,Intersection End World Position,Intersection End Depth ,0-1 Sphere density,Projected Capture Vector 
F|RGBtoHSV@/Engine/Functions/Engine_MaterialFunctions02/Math/RGBtoHSV.RGBtoHSV|Converts RGB colors to HSV (hue saturation and value)|I:*|O:*
F|Round|Rounds a number to the next closest whole number|I:*|O:*
F|SafeNormalize|If the input vectors length == 0 then return 0 else ret…|I:Vector,Default|O:Result,Length==0
F|Sign|Returns a -1 for negative numbers, a 1 for positive num…|I:*|O:*
F|Sine_Remapped|remaps the output of a sine wave to two colors/vectors…|I:Sine Phase,Value 1,Value 2|O:*
F|SumOfAConsecutiveNumberSequence|This will find the sum of numbers up to the integer ins…|I:*|O:*
F|Transform3x3Matrix|Transform a vector into a new basis|I:VectorToTransform,BasisX,BasisY,BasisZ,BasisPosition|O:*
F|TransformToClipSpace@/Engine/Functions/Engine_MaterialFunctions02/Math/TransformToClipSpace.TransformToClipSpace|Transforms a world position into clip space (render buf…|I:*|O:*
F|TransformToClipSpace@/Engine/Functions/Engine_MaterialFunctions02/TransformToClipSpace.TransformToClipSpace|-|I:World Position,Buffer UV Pixel Offset|O:Buffer UVs for Scene Textures,Screen aligned 0-1 UV,Clip Space XY
F|UnpackNormalFromFloat|Unpack Normal/Float3 values from a scalar value|I:*|O:( z sign ) XXYY.0,XXY.YZZ Normalized Vector,XXY.YZZ Vector,( z sign ) XXX.YYY Normal
F|VectorToRadialValue|The input coordinates or vector will be transformed int…|I:Swizzle Coordinate Output,Vector or UVs|O:Radial Coordinates,Vector Converted to Angle,Linear Distance
F|MS_MultiNormal_UVnormals|This material function was designed to be used in conju…|I:-|O:Tangent Space UVs,Custom UV 4,Custom UV 5
F|MS_MultiNormal_VertexColorNormals|This material function was designed to be used in conju…|I:-|O:*
F|MS_SequencePainter_Sequence|-|I:-|O:*
F|MS_SequencePainter_SequenceFlipbook|This function will create a mesh flipbook from assets p…|I:0-1 Animation,Number Of Frames|O:*
F|SpiralBlur-SceneTexture|Performs a Spiral Blur with controllable number of step…|I:Distance,Distance Steps,Radial Steps,Radial Offset,TempAA Radial Blur,TempAA Distance Blur,Distance Mask|O:Result,SceneColor clamp to 0
F|SpiralBlur-Texture|Performs a Spiral Blur with controllable number of step…|I:TextureObject,UV,Distance,Distance Steps,Radial Steps,Radial Offset,Kernel Power|O:*
F|BlendAngleCorrectedNormals|Corrects the normal direction of normal map that is ove…|I:BaseNormal,AdditionalNormal|O:*
F|RotateNormalWhileMasking|This will rotate a normal toward it's slope as the grey…|I:Hp Normal,Grey Scale Mask Amount,LowPolyNormal|O:*
F|SoftOpacity|Softens the Opacity input by multiplying against Fresne…|I:DepthFadeDistance,OpacityIn,FadeDistance|O:OutputUsesDepthBias,OutputNoDepthBias
F|3dParticleOpacity|-|I:Depth Texture,-------------Depth Texture Options-----------,Use dynamic (True) or explicit texture depth settings (False),Dynamic Texture Depth Ratio,Explicit Texture Depth (WS),Depth Texture Falloff Softness (WS) (1/n),-------Camera Falloff Group-------,Near Camera Falloff Start Distance,Use Near Camera Falloff,Near Camera Fade Distance (1/n),Use Depth In Camera Falloff Calculation,-------Particle Alpha Group-------,Use Particle Alpha,-------WPO Group-------,Camera Offset|O:Opacity,World Position Offset - Camera Offset
F|Distance_Blend|Sets a distance and range to blend from 0 to 1|I:Blend Range,Start Offset|O:*
F|RandomUVs|Uses a DynamicParameter with U_Offset and V_Offset as p…|I:*|O:*
F|GeneratedBand|Procedurally generates a horizontal or vertical band fr…|I:Compare,Direction Switch,Input Coordinates,Offset,Sharpness,Width|O:*
F|GeneratedOffsetBands|Procedurally generates a horizontal or vertical band fr…|I:Bands,Compare,Direction Switch,Input Coordinates,Offset,Sharpness,Width|O:*
F|NormalFromFunction|Takes a heightmap input and generates a normal map from…|I:Coordinates,Height Map UV Offset,Normal Map Intensity,Function(UV1),Function(UV2),Function(UV3)|O:Normal,UV1,UV2,UV3
F|NormalFromHeightmap|Takes a heightmap input and generates a normal map from…|I:Height Map,Normal Map Intensity,Height Map UV Offset,Coordinates,Height Map Channel Selector|O:*
F|NormalFromHeightmapChaos|EXPENSIVE - Takes a heightmap input, pans it 4 ways and…|I:Coordinates,Height,Height Bias|O:*
F|ObjectSpaceFalloff|Derives a falloff based on object's location.|I:Aspect Ratio - U,Aspect Ratio - V,Falloff Hardness,Falloff Scale,Invert 1st Channel,Invert 2nd channel,Offset - U,Offset - V,Offset Transform Switch,Projection Transform Switch|O:*
F|CustomReflectionVector|Input a normal to generate a reflection vector independ…|I:Normal,CameraVector|O:*
F|ReflectionVectorSoft|Softens the normal for a smoother reflection|I:Normal,Softness|O:*
F|ViewAlignedReflection|Alignes a Reflection texture to your view.|I:ReflectionTexture,ReflectionVector|O:Texture,UVs
F|WorldAlignedReflection|Alignes a Reflection texture to your view.|I:ReflectionTexture,ReflectionVector|O:WorldReflection,WorldReflectionShadowed
F|CalcLightsourceAngle|This function can be used to calculate the light source…|I:Light Position,Source Radius|O:Degrees,Radians
F|Ellipsoid-ConeShadow-Texture|Returns the occlusion value for a pixel given a sphere…|I:Light Vector,Ellipsoid Position,Ellipsoid XY size,Light Source Angle,Ellipsoid Z Scale,Ellipsoid X Axis,Ellipsoid Y Axis,Ellipsoid Z Axis,Is Light Directional|O:*
F|FuzzyShading|This function emulates shading simmilar to velvet or mo…|I:BaseColor,Normal,CoreDarkness,EdgeBrightness,Power|O:*
F|FuzzyShadingGrass|This function is the diffuse portion of grass shading.|I:Diffuse,EdgeColor,EdgeDesat,Normal,CoreDarkness,EdgeBrightness,Power|O:*
F|MetallicShading|Apply to base color of metals for more interesting shad…|I:*|O:*
F|Sphere-ConeShadow-Texture|Returns the occlusion value for a pixel given a sphere…|I:Light Vector,Sphere Position,Sphere Radius,Light Source Angle|O:*
F|Sphere_AO|This function can be used to calculate the Ambient Occl…|I:Sphere Position,Source Radius|O:*
F|Spherical-Cap-Intersection|Mathematically computes the area of two spherecap inter…|I:Angle Between Cones,View Occlusion Angle,Light Source Angle,Use Smoothstep,Use Radians|O:Illumination,Area of intersection
F|TextureDefinedSpecularShape|Aligns the Highlight shape to the reflected light|I:HighlightShape,Normal,SpecularIntensity,SpecularSharpness|O:*
F|SpeedTreeColorVariation|Adds a color variation per object/instance to break up…|I:BaseColor,Amount|O:*
F|3DParticleUVs|Moves through a flipbook texture based on the cameras p…|I:Number of horizontal Images,Number of texture rotations per world rotation,UVs|O:*
F|3DSandMayaUVCoordinates|Inverts the green channel in each set of model uvs to p…|I:-|O:UVChannel0,UVChannel1,UVChannel2,UVChannel3
F|AbberatedBlur-Texture|Blurs a Texture along a specified 2D Axis with chromati…|I:TextureObject,UV,Vector,Distance,Steps|O:*
F|BitMask|Provides a 1bit mask from a supplied Grayscale image an…|I:Bit,BitMask|O:*
F|BumpOffset_advanced|-|I:HeightTexture,TextureCoordinates,ReferencePlane,HeightRatioInput,CameraVector|O:Undeformed UVs,UVs,Distortion
F|CameraWorldBlend|Outputs falloff results for the 3 primary world vectors…|I:Blend Power,Use Reflection Vector,Use Smoothable Normals,Smooth Reflection Percentage|O:XY True,XZ True,YZ True
F|CustomRotator|Rotator with rotation center exposed and a rotation ang…|I:UVs,Rotation Center,Rotation Angle (0-1)|O:*
F|CylindricalUVs|Tiles a texture using Cylindrical UVS centered around O…|I:In,Normal,TextureObject|O:Cylinder Projection,Cylinder Projection w Top
F|DetailTexturing|-|I:Scale,Diffuse,DetailDiffuse,DiffuseIntensity,Normal,DetailNormal,NormalIntensity|O:Diffuse,Normal
F|DistanceField|Reads a Distance field texture|I:DistanceField,EdgeSoftness|O:*
F|FlattenNormal|Lerps a NormalMap with 0,0,1|I:Normal,Flatness|O:*
F|FlowMaps|Pushes the Diffuse and Normal textures along the flow m…|I:Diffuse,Normal Map,Flow Vector Map (see tooltip),UV texture 2 offset,Time (see tooltip),useMipLevel,UVs,Texture Size,Texture Mip Bias|O:Diffuse,Diffuse Alpha,Normal,Distortion,UVs
F|FlowMaps_Simple|Pushes the Diffuse and Normal textures along the flow m…|I:Diffuse,Normal Map,Flow Vector Map (see tooltip),UV texture 2 offset,Time (see tooltip),UVs|O:Diffuse,Diffuse Alpha,Normal,Distortion
F|FlowMaps_UV1|Pushes the Diffuse and Normal textures along the flow m…|I:Diffuse,Normal Map,Flow Vector Map (see tooltip),UV texture 2 offset,Time (see tooltip),UVs,Texture Size,Texture Mip Bias|O:Diffuse,Diffuse Alpha,Normal,Distortion
F|HeightLerp|Lerp between two values or textures based off of a heig…|I:A,B,Transition Phase,Height Texture,Contrast|O:Results,Alpha,Lerp Alpha No Contrast
F|HeightLerpWithTwoHeightMaps|Lerp between two values or textures based off of two he…|I:Diffuse 1,Diffuse 2,Transistion Phase,Height Texture 1,Height Texture 2,Contrast|O:Results,Alpha,Lerp Alpha No Contrast,Resulting Height Map
F|HighPrecisionWorldPosTextureSampling|Provides a world position that can be used to map textu…|I:Texture Object,TilingSize,Texture Coord U Vector,Texture Coord V Vector|O:Texture (F4),High Precision World Position
F|LocalAlignedTexture|Tiles a texture in worldspace|I:Normal,TextureObject|O:XY Texture,XYZ Texture,Z Texture
F|LocalAlignedTexture_TransformedWorldSpace|Tiles a texture in worldspace|I:Normal,TextureObject|O:XY Texture,XYZ Texture,Z Texture
F|LocalSpaceSurfaceMirroring|Generates mask results based on the local orientation o…|I:In,Normal Map,Use NormalMap|O:Local X,Local Y,Local Z
F|MosaicUVs|Creates a mosaic style effect where the texture will be…|I:UVs,Tiles|O:*
F|MotionBlur-Texture|Blurs a Texture along a specified 2D Axis|I:TextureObject,UV,Vector,Distance,Steps|O:Result,Results with Chromatic Shift
F|PackedDistanceField|Reads Distance Field textures packed as a subUV|I:PackedDistanceField,UVs,ImageCount,EdgeSoftness,ImageNumber|O:*
F|ParallaxOcclusionMapping|Parallax Occlusion Mapping uses Ray Tracing to find the…|I:Heightmap Texture,Height Ratio,Min Steps,Max Steps,UVs,Heightmap Channel,Reference Plane,-----------------------------,Use World Coordinates,Specify Manual Texture Size,Manual Texture Size,------------------------------,Render Shadows (Occlusion Mapping),Light Vector,Shadow Steps,Shadow Penumbra,Transform To VertexNormal|O:Parallax UVs,Offset Only,Shadow,Pixel Depth Offset,World Position,Tangent Light Vector,Material Complexity - Steps Debug
F|ParallaxOcclusionMapping_BoundedUVs|Parallax Occlusion Mapping uses Ray Tracing to find the…|I:Heightmap Texture,Height Ratio,Min Steps,Max Steps,UVs,Heightmap Channel,Reference Plane,-----------------------------,Use World Coordinates,Specify Manual Texture Size,Manual Texture Size,ClampMinMax,Ray Direction,Transform To VertexNormal|O:Parallax UVs,Intersection Mask,Offset Only,Pixel Depth Offset,World Position,Material Complexity - Steps Debug
F|ScreenAlignedPixelToPixelUVs|Maps a texture to the screen without stretching any of…|I:*|O:*
F|ScreenAlignedUVs|Maps the 0-1 uv range to the screen.|I:*|O:X 100%, Y 100%,X 100%, Y Scale to Ratio,X Scale to Ratio, Y 100%
F|SkyAtmosphereImage|-|I:TextureObject,Direction,Scale,Rotation (radian)|O:Result,Alpha,Mask
F|SkyboxImage|Projects an image onto an infinite sphere, useful for p…|I:TextureObject,ImageVector,Scale,Rotation 0-1|O:RGB,Alpha,Mask
F|SlopeMask|Slopemask, useful for stuff like snow, moss|I:TangentNormal,SlopAngle,FalloffPower,CheapContrast|O:*
F|SteppingPannerTime|Add to UV coordinates to make them jump by the "Jump Am…|I:Jump Amount Per Step,Number of Steps Per Unit of Time,TimeSpeed,Time Offset|O:*
F|SubUV_Function|Allows SubUV blending of multiple texture frames in a s…|I:Texture,UVs,SubImages,Frame|O:Alpha,RGB,UVs
F|SubUV_Function_MipDerivative|Allows SubUV blending of multiple texture frames in a s…|I:Texture,UVs,SubImages,Frame|O:Alpha,RGB,UVs
F|TangentSpaceFlow|Pushing the FlowTexture along the direction of the Flow…|I:Export Float 4,FlowDirection,FlowSpeed,FlowStrength,FlowTexture,UVs|O:*
F|TangentSpaceFlowComplex@/Engine/Functions/Engine_MaterialFunctions01/Texturing/TangentSpaceFlowComplex.TangentSpaceFlowComplex|Pushing the FlowTexture along the direction of the Flow…|I:FlowDirection,FlowSpeed,FlowStrength,FlowTexture,UVs,Time,MipBias|O:Result,Uv1,Uv2,LerpAlpha
F|TangentSpaceFlowComplex@/Engine/Functions/Engine_MaterialFunctions02/Texturing/TangentSpaceFlowComplex.TangentSpaceFlowComplex|Pushing the FlowTexture along the direction of the Flow…|I:FlowMap,FlowTexture,UVs,Anim offset Noise,Time|O:*
F|TextureCropping|Crops a texture, useful for Emissives.|I:TextureIn,UVs,UpperLeftCorner,LowerRightCorner,ExportFloat4|O:Cropped,CroppedMasked,Crop UVs,Crop Mask
F|TriplanarCameraVector|Applies a texture to the background, similar to a cubem…|I:CameraVector,Texture,Tiling,Offset,AxisFadeContrast|O:*
F|TwoSidedTexturing|Gives independent texturing control for both sides of a…|I:Texture Side A,Texture Side B|O:Texture Blend Output,Mask
F|VectorDisplacement|Use a Baked Vector displacement map from Xnormal|I:Vector,ScalarDisplacement,Min,Max|O:*
F|WorldAlignedNormal|Tiles a texture in worldspace|I:Normal,TextureObject,TextureSize,WorldSpace,ProjectionTransitionContrast,WorldPosition,Use High Quality Normals|O:XY Texture,XYZ Texture,XYZFlatTop,Z Texture
F|WorldAlignedNormal2|Tiles a texture in worldspace|I:Normal,TextureObject,TextureSize|O:XY Texture,XYZ Texture,XYZFlatTop,Z Texture
F|WorldAlignedNormals_HighQuality|Applies normal maps to objects and correctly orients th…|I:Negative World Position Divisor,Texture,World Position,Z lerp Alpha,WorldNormal,X lerp alpha|O:World Space Normals XYZ,XY Flat Top Projection World Space Normals,XY Projection World Space Normals,Z Projection World Space Normals
F|WorldAlignedNormals_HighQuality_optimizationAttempt@/Engine/Functions/Engine_MaterialFunctions02/NotInUse/WorldAlignedNormals_HighQuality_optimizationAttempt.WorldAlignedNormals_HighQuality_optimizationAttempt|Applies normal maps to objects and correctly orients th…|I:Negative World Position Divisor,Texture,World Position,Z lerp Alpha,WorldNormal,X lerp alpha,Optimize (See Comment)|O:World Space Normals XYZ,XY Flat Top Projection World Space Normals,XY Projection World Space Normals,Z Projection World Space Normals,UV2,UV3,UV4,UV5,UV6,UV7
F|WorldAlignedNormals_HighQuality_optimizationAttempt@/Engine/Functions/Engine_MaterialFunctions02/WorldAlignedNormals_HighQuality_optimizationAttempt.WorldAlignedNormals_HighQuality_optimizationAttempt|Applies normal maps to objects and correctly orients th…|I:Negative World Position Divisor,Texture,World Position,Z lerp Alpha,WorldNormal,X lerp alpha,Optimize (See Comment)|O:World Space Normals XYZ,XY Flat Top Projection World Space Normals,XY Projection World Space Normals,Z Projection World Space Normals,UV2,UV3,UV4,UV5,UV6,UV7
F|WorldAlignedTexture|Tiles a texture in worldspace|I:Export Float 4,TextureObject,TextureSize,World Space Normal,WorldPosition,ProjectionTransitionContrast|O:XY Texture,XYZ Texture,Z Texture
F|WorldAlignedTexture_MipBias|Tiles a texture in worldspace|I:Export Float 4,TextureObject,TextureSize,World Space Normal,WorldPosition,MipBias,ProjectionTransitionContrast|O:XY Texture,XYZ Texture,Z Texture
F|WorldAlignedTexture_SeperateChannels|Tiles a texture in worldspace|I:TextureObject,TextureSize (R),TextureSize (G),TextureSize (B),World Space Normal,WorldPosition,ProjectionTransitionContrast|O:Z Texture (R),XY Texture (R),XYZ Texture (R),Z Texture (G),XY Texture (G),XYZ Texture (G),Z Texture (B),XY Texture (B),XYZ Texture (B)
F|WorldAlignedTextures_Complex|Tiles a texture in worldspace|I:Diffuse Texture Object,Spec Texture Object,TextureSize,--------------------------,Texture Size Z projection,Use seperate settings for Z projection,Use seperate texture for Z projection,Z Plane Diffuse Texture Object,Z Plane Spec Texture Object,--------------------------      ,ProjectionTransitionContrast,Use Texture Alpha Heightmap to Refine the Transistion,HeightLerpTransitionContrast,PickTheDiffuseHeightChannel,TheDiffuseHeightChannel,--------------------------       ,NormalTextureObject,World Space Normals,--------------------------  ,Export Float 4 Diffuse,Export Float 4 Spec,--------------------------     ,WorldPosition,World Space Normal|O:XYZ Diffuse Texture,XY Diffuse Texture,Z Diffuse Texture,-------------------------- ,XYZ Spec,XY Spec,Z Spec, --------------------------,Normal XYZ Texture,Normal XYZ Flat Top,Normal XY Texture,Normal Z Texture,  --------------------------,XYZ Mat Attributes - See Tooltip,XY Mat Attributes - See Tooltip,Z Mat Attributes - See Tooltip
F|WorldAlignedTextures_Complex_OptimizationAttempt@/Engine/Functions/Engine_MaterialFunctions02/NotInUse/WorldAlignedTextures_Complex_OptimizationAttempt.WorldAlignedTextures_Complex_OptimizationAttempt|Tiles a texture in worldspace|I:Diffuse Texture Object,TextureSize,-------------,Texture Size Z projection,Use seperate settings for Z projection,Use seperate texture for Z projection,Z Plane Diffuse Texture Object,      -------------,ProjectionTransitionContrast,Use Texture Alpha Heightmap to Refine the Transistion,HeightLerpTransitionContrast,PickTheDiffuseHeightChannel,TheDiffuseHeightChannel,    -------------,NormalTextureObject,OptimizeHighQualityNormals (see comment),UseHighQualityNormals,World Space Normals,  -------------,Export Float 4,     -------------,WorldPosition,World Space Normal|O:XYZ Diffuse Texture,XY Diffuse Texture,Z Diffuse Texture,-------------,Normal XYZ Texture,Normal XYZ Flat Top,Normal XY Texture,Normal Z Texture,-------,Opti Normal - Custom UV 2,Opti Normal - Custom UV 3,Opti Normal - Custom UV 4,Opti Normal - Custom UV 5,Opti Normal - Custom UV 6,Opti Normal - Custom UV 7
F|WorldAlignedTextures_Complex_OptimizationAttempt@/Engine/Functions/Engine_MaterialFunctions02/Texturing/WorldAlignedTextures_Complex_OptimizationAttempt.WorldAlignedTextures_Complex_OptimizationAttempt|Tiles a texture in worldspace|I:Diffuse Texture Object,TextureSize,-------------,Texture Size Z projection,Use seperate settings for Z projection,Use seperate texture for Z projection,Z Plane Diffuse Texture Object,      -------------,ProjectionTransitionContrast,Use Texture Alpha Heightmap to Refine the Transistion,HeightLerpTransitionContrast,PickTheDiffuseHeightChannel,TheDiffuseHeightChannel,    -------------,NormalTextureObject,OptimizeHighQualityNormals (see comment),UseHighQualityNormals,World Space Normals,  -------------,Export Float 4,     -------------,WorldPosition,World Space Normal|O:XYZ Diffuse Texture,XY Diffuse Texture,Z Diffuse Texture,-------------,Normal XYZ Texture,Normal XYZ Flat Top,Normal XY Texture,Normal Z Texture,-------,Opti Normal - Custom UV 2,Opti Normal - Custom UV 3,Opti Normal - Custom UV 4,Opti Normal - Custom UV 5,Opti Normal - Custom UV 6,Opti Normal - Custom UV 7
F|WorldCoordinate3Way|Takes textures and projects them in world-space onto th…|I:XY Texture,XZ Texture,YZ Texture,XY Scale,XZ Scale,YZ Scale,Blend Exponent Y Z,Blend Mult Y Z,Blend Exponent X,Blend Mult X,Single Texture,Normal,WorldPosition|O:XYZ Output,XY,XZ,YZ
F|WorldPositionBehindFromDepth_experimental|This will recreate the scenes world position behind a t…|I:*|O:*
F|WorldPositionBehindTranslucency|This will recreate the scenes world position behind a t…|I:SceneDepth,Exclude WPO Offsets|O:*
F|WorldPositionWithScale|WorldPosition divided by a number and split into common…|I:*|O:XYZ,XY,Z
F|ZWorldSpaceFlow|Pushing the FlowTexture along the direction of the Flow…|I:FlowDirection,FlowSpeed,FlowStrength,FlowTexture,TextureSize,WorldPosition|O:*
F|BoxMask-2D|Draws a box in 2D Space.|I:A,B,Bounds,Edge Falloff|O:*
F|BoxMask-3D|Draws a box in 3D Space.|I:A,B,Bounds,Edge Falloff|O:*
F|GeneratedRoundRect|Draws a box in 2D Space.|I:UV Coords,Box Dimensions,CornerRadius,Center,Sharpness|O:*
F|Fresnel_Function|Fresnel with more properties exposed, less instructions…|I:Normal Vector,Camera Vector,Invert Fresnel,Power,Use Cheap contrast,Cheap contrast dark,Cheap contrast bright,Clamp Fresnel Dot Product|O:*
F|CameraDirectionVector|World space vector of the camera direction.|I:-|O:*
F|CameraVectorWithWPOOptions|Retrieves the camera vector with or without vertex shad…|I:*|O:*
F|RotateVector|Rotates an input vector to point toward a given directi…|I:VectorToRotate,LookAtVector,RestingVector|O:*
F|AppendMany|Allows you to quickly append up to 4 scalars in one fun…|I:R,G,B,A|O:RG,RGB,RGBA
F|AlignMeshToTheCamera|Aligns a static mesh to the camera and allows the user…|I:PivotLocation,WorldPosition,WS Normals,Custom Object Basis 1,Custom Object Basis 2,Custom Object Basis 3|O:Rotated Normals,CameraXVector,test WPO,World Position Offset,Undeformed Pixel Shader World Position
F|AttachMeshToTheCamera|Attaches a static mesh to the camera and allows the use…|I:Object Basis 1,Object Basis 2,Object Basis 3,Camera Space Position Offset|O:*
F|CameraOffset|Offset objects in the direction of the camera to either…|I:Offset Amount,Clamp Padding,World Position|O:Clamped Camera Offset,Camera Offset
F|CanopyCreator_Branches|This function widens strips of polies along the U of th…|I:WidthBase,WidthTip,WorldPosition,UVs for Projection,UVs for Thickness,UVs for texturing,Expand U or V UV Channel,DeriveNormalZ,AdditionalNormal,AngleCorrectedNormals,FlattenPixelNormal,UVs For NormalShading|O:Normal,WorldPositionOffset,UVs with Parallax
F|CenterPivotAroundVector|Returns world position for every vertex as it would be…|I:*|O:LocalPosition,WorldPosition
F|ConstantScalebyDistance|Keeps a quad a constant scale on the screen, falls apar…|I:*|O:*
F|DropletParticleVertexShader|Make a camera aligned particle distort like a raindrop…|I:Speed Per unit of tail distortion,Distortion lerp rate,Max tail lengthing percentage,Min speed before distortion|O:*
F|FixRotateAboutAxisNormals|Use this material function in conjunction with a rotate…|I:Rotation Axis,Rotation Angle,World Space Vertex Normals,Movement Mask,PivotPoint|O:New Tangent Space Vertex Normal,New Tangent Space Vertex Normal RG,New Tangent Space Vertex Normal B,New World Space Vertex Normal
F|FixRotateAboutAxisNormals2|Use this material function in conjunction with a rotate…|I:Rotation Axis,Rotation Angle,World Space Vertex Normals,Movement Mask|O:New Tangent Space Vertex Normal,New Tangent Space Vertex Normal RG,New Tangent Space Vertex Normal B,New World Space Vertex Normal
F|GenerateASpline|Generate a Catmull-Rom spline.|I:t,P0,P1,P2,P3,Normal/Bi-Normal Cross product vector|O:UnnormalizedTangent,T Bi-normal,T Normal,T position,T Tangent
F|MS_CanopyCreatorMeshExpansion|This function widens strips of polies along the U of th…|I:WorldPosition,Normal Map|O:Normal,WorldPositionOffset,Black=Spline Thicken White=Normal,white = knots black = everything else,Branch Radius
F|ObjectPivotPoint|Returns the object's pivot point in world space.|I:-|O:Object Pivot Location,Mesh Particle Pivot Location
F|ObjectScale@/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/ObjectScale.ObjectScale|Returns the object's XYZ scale together and seperately.…|I:-|O:Scale XYZ,Scale X,Scale Y,Scale Z
F|ObjectScale@/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/V2/ObjectScale.ObjectScale|Returns the object's XYZ scale together and seperately.…|I:-|O:Scale XYZ,Scale X,Scale Y,Scale Z
F|PivotAxis|Creates a common pivot location on arbitrary axes.|I:*|O:*
F|RotateAboutWorldAxis_cheap|This function cheaply rotates objects around world axes.|I:Rotation Amount,PivotPoint,WorldPosition|O:X-Axis,Y-Axis,Z-Axis
F|SimpleGrassWind|Simple Waving grass wind, Grass must be textured to ful…|I:AdditionalWPO,WindIntensity,WindSpeed,WindWeight|O:*
F|SineWithNormalSupport|Very specific material function that projects into worl…|I:Rotation fudge factor,X world dot,Y world dot,time,World Position|O:Sine Wave World Normal,SineWave
F|SplineBasedModelDeformation|Deform a model around a spline that is created with the…|I:P0,P1,P2,P3,Thickness,LocalDeformationVector,Model height along deformation vector,Local Position,Optional Tangent Space Normal Map,Optional Greyscale Height Map|O:World Position Offset,Local Position Offset,BiNormal (X),Normal (Y),Tangent (Z),World T Position,Pixel normal (WS Cylindrical),Pixel normal (WS Texture),Debug Gradient
F|SplineThicken|This function widens strips of polies along the U of th…|I:WidthBase,WidthTip,WorldPosition,UVs for Projection,UVs for Thickness,UVs for texturing,Expand U or V UV Channel,DeriveNormalZ,AdditionalNormal,AngleCorrectedNormals,FlattenPixelNormal,UVs For NormalShading|O:Normal,WorldPositionOffset,UVs with Parallax
F|Sprite|Use this function within the world position offset inpu…|I:0-1 UVs,Center Location,XY scale,OverridePivot,Normals (Optional)|O:World position offset,Normals
F|StaticMeshMorphTargets|Unpacks Morph Data From the 3ds Max Morph Packer Script|I:-|O:Morph Target 1 Normals,---------------,Morph Target 1 WPO,Morph Target 2 WPO,Pivot Position WS
F|UVLayoutToWorldSpacePosition|Use in the world position offset input to visual uv coo…|I:*|O:*
F|Wind|Seperate outputs for wind strength, speed multiplied by…|I:*|O:Normalized Wind Vector,Wind Strength,WindSpeed,WindActor
F|HeightToNormalSmooth|Provide perpixel height data and return a partially smo…|I:Height,Absolute World Position,World Space Vertex Normals|O:*
F|Chroma_Key_Alpha|Extracts an alpha mask from a chroma key aka green scre…|I:Image Color,LumaMask,Chroma Color,Alpha Cutoff Min,Alpha Cutoff Max,Alpha Exponent,Despill Cuttoff Max,Despill Exponent|O:Alpha,Despill Alpha,Raw Comparison
F|ParticleSizeByPixelUnits|This function replaces the vertex shader for sprite par…|I:Size In Pixels,ParticlePosition,ScreenSpace Pivot Offset,Normals (Optional)|O:Normals,World Position Offset,World Position Offset With Pivot Support
F|PivotPainter_HierarchyData|Processes and organizes world position and angle inform…|I:*|O:Parent Piv Position,Parent X Axis Vector,------------------------,Child Piv Position,Child X-Axis Vector,------------------------ ,Object  Pivot Point,Object Orientation,Object Scale,Black Mask
F|PivotPainter_PerObjectData|Processes and organizes world position and angle inform…|I:-|O:X-Axis Vector,Pivot Position,Random Value Per Element,Custom Alpha Values,Object Scale,Black Mask
F|PivotPainter_PerObjectFoliageData|Processes and organizes world position and angle inform…|I:Optimized for Foliage Placement,Wind Vector,Optimized Vector|O:Piv Position,Element Rot Axis,Element X-Axis,Random Value Per Element,Custom Alpha Values,Normalized Wind Vector,Wind Accumulator,Wind Speed,Wind Strength,Object PIvot Location,Object Scale XYZ,Uniform Object Scale
F|PivotPainter_TreeData|Processes and organizes world position and angle inform…|I:Max Dist for Parent Piv,WindVector|O:Branch Piv Position,Branch Wind Rot Axis,Branch-X Axis Vector,Branch flow Grad,Branch flow Grad 90 deg,------------------------,Leaf Piv Position,Leaf Rot Axis,Leaf X-Axis Vector,Leaf Mask,Leaf flow Grad,Leaf flow Grad 90 deg,------------------------ ,Object  Pivot Point,Object Orientation,Object Rotation Axis,Object Scale,Object Flow Grad,Object Flow Grad 90 deg,------------------------  ,WindStrength,Normalized Wind Vector,WindSpeed,------------------------   ,Black Mask
F|ms_PivotPainter2_CalculateMeshElementIndex|Pulls the model elements element ID from the models uvs.|I:Data Texture Dimensions,Pivot Painter UV Coordinates|O:*
F|ms_PivotPainter2_Decode8BitAlphaAxisExtent|Rescale 8 bit axis extent texture data information from…|I:*|O:*
F|ms_PivotPainter2_DecodeAxisVector|Transforms Pivot Painter 2.0's local space vector info…|I:*|O:*
F|ms_PivotPainter2_DecodePostion|Transforms Pivot Painter 2.0's local space position inf…|I:*|O:*
F|ms_PivotPainter2_ReturnParentTextureInfo|Read a parent sub object's texture data using Pivot Pai…|I:Parent Index As Float (See note),Texture Dimensions,Current Index (see note)|O:Parent UVs,Is Child? (See note)
F|ms_PivotPainter2_UnpackIntegerAsFloat|Decodes Pivot Painter Integer As Float Data|I:*|O:*
F|PivotPainter2FoliageShader|This material function contains texture and numeric par…|I:Material Attributes (See Note),Pivot Painter Texture Coordinate|O:Final Material with World Space Normals,Modified World Space Normal Component,World Position Offset Component
F|DistanceLimitedReflections|Distance Limited Reflections give some parallax to cube…|I:Cubemap,CapturePosition,Radius|O:Result,Sphere Hit Mask
F|AxisAlignedFresnel|Gives a fresnel type falloff that is only perpendicular…|I:Axis,Exponent,Normal|O:Fresnel,Cylinder Thickness
F|SpeedTreeBillboardNormals|Move normals into screen space for smoother billboard l…|I:*|O:*
F|SpeedTreeCrossfadeBillboard|Handles crossfading between billboard faces|I:*|O:OpacityMask,CustomUV
F|MF_Substrate_OpenPBR_Opaque|-|I:----| Base |----,base_weight,base_color,base_roughness,base_metalness,----| Specular |----,specular_weight,specular_color,specular_roughness,specular_ior,specular_ior_level,specular_anisotropy,specular_rotation,----| Subsurface |----,subsurface_weight,subsurface_color,subsurface_radius,subsurface_radius_scale,subsurface_anisotropy,----| Coat |----,coat_weight,coat_color,coat_roughness,coat_ior,coat_ior_level,coat_anisotropy,coat_rotation,----| Fuzz |----,fuzz_weight,fuzz_color,fuzz_roughness,----| Emission |----,emission_luminance,emission_color,----| Thin Film |----,thin_film_thickness,thin_film_ior,----| Geometry |----,geometry_opacity,geometry_normal,geometry_tangent,geometry_coat_normal|O:OpenPBR_FrontMaterial,OpacityMask
F|MF_Substrate_OpenPBR_Translucent|-|I:----| Base |----,base_weight,base_color,base_roughness,base_metalness,----| Specular |----,specular_weight,specular_color,specular_roughness,specular_ior,specular_ior_level,specular_anisotropy,specular_rotation,----| Transmission |----,transmission_weight,transmission_color,transmission_depth,transmission_scatter,transmission_scatter_anisotropy,transmission_dispersion_scale,transmission_dispersion_abbe_number,----| Coat |----,coat_weight,coat_color,coat_roughness,coat_ior,coat_ior_level,coat_anisotropy,coat_rotation,----| Fuzz |----,fuzz_weight,fuzz_color,fuzz_roughness,----| Emission |----,emission_luminance,emission_color,----| Thin Film |----,thin_film_thickness,thin_film_ior,----| Geometry |----,geometry_opacity,geometry_normal,geometry_tangent,geometry_coat_normal|O:OpenPBR_FrontMaterial,OpacityMask
F|Substrate Coated Layer|-|I:Coat Specular,Coat Roughness,Coat Normal,Coat Color,Coat Emissive Color,Thickness factor,Base Color,Metallic,Specular,Roughness,Normal,Emissive Color,Opacity|O:*
F|Substrate Standard Surface Opaque|Opaque Standard Surface|I:----|  Base  |----,base,base_color,diffuse_roughness,metalness,----|  Specular  |----,specular,specular_color,specular_roughness,specular_IOR,specular_anisotropy,specular_rotation,----|  Subsurface  |----,subsurface,subsurface_color,subsurface_radius,subsurface_scale,subsurface_anisotropy,----|  Coat  |----,coat,coat_color,coat_roughness,coat_IOR,coat_anisotropy,coat_rotation,coat_normal,----|  Sheen  |----,sheen,sheen_color,sheen_roughness,----|  Emission  |----,emission,emission_color,----|  Thin Film  |----,thin_film_thickness,thin_film_IOR,----|  Geometry  |----,opacity,normal,tangent|O:Substrate StandardSurface Opaque,Geometry Opacity
F|Substrate Standard Surface Translucent|Translucent Standard Surface|I:----|  Base  |----,base,base_color,diffuse_roughness,metalness,----|  Specular  |----,specular,specular_color,specular_roughness,specular_IOR,specular_anisotropy,specular_rotation,----|  Transmission  |----,transmission,transmission_color,transmission_depth,transmission_scatter,transmission_extra_roughness,----|  Coat  |----,coat,coat_color,coat_roughness,coat_IOR,coat_anisotropy,coat_rotation,coat_normal,----|  Sheen  |----,sheen,sheen_color,sheen_roughness,----|  Emission  |----,emission,emission_color,----|  Thin-Film  |----,thin_film_thickness,thin_film_IOR,----|  Geometry  |----,opacity,normal,tangent|O:Substrate StandardSurface Opaque,Geometry Opacity
F|Substrate UE4 Default Shading|-|I:Base Color,Metallic,Specular,Roughness,Normal,Emissive Color,Opacity|O:*
F|Substrate UE4 Unlit Shading|Unlit material with Opacity input.|I:Color,Opacity|O:*
F|Substrate FlipFlop|-|I:F0,F90,Falloff,WorldNormal|O:Result,LerpFactor
F|Substrate IOR-To-F0|Convert a dieletric IOR into a F0 value.|I:*|O:*
F|Substrate Rotation-To-Tangent|Convert a rotation angle into a tangent vector|I:*|O:*
F|Substrate View-Dependent-Coverage|-|I:Coverage,Normal,Thickness|O:Coverage,Thickness
F|BrickAndTileUVs|Bricks and Tile UVs create a semi procedural UV offset…|I:UV,Tiles X,Tiles Y,Tile Shift,Texture Tiling,Macro Tiling,Rotate 90,Pattern Distortion|O:DiffuseUVs,MacroUVs,Macro Offsets only,TileUVs
F|Flowmaps_2D|This 2D version of flowmaps is designed to be the 2D ve…|I:Volume Texture,UV,Velocity,Override Time,Mip Level|O:Result RGB,Result RGBA
F|Flowmaps_3D|Performs Flowmap blending using a Volume Texture.|I:Volume Texture,UVW,Velocity,Override Time,Mip Level|O:Result RGB,Result RGBA
F|StretchGradient|A 0-1 uv gradient is scaled by a desired amount while r…|I:0-1 Gradient,Center Point,Scale Factor|O:Resulting Gradient,Clamped area
F|Texture_Bombing|Texture bombing uses multiple offset texture samples to…|I:Texture Object,UVs,Tiling,Offset,Optional Heightmap,Contrast,Enable Height Lerp,Is Normalmap|O:*
F|Texture_Bombing_POM|Texture bombing uses multiple offset texture samples to…|I:Texture Object,UVs,Tiling,Offset,Optional Heightmap,Contrast,Enable Height Lerp,HeightRatio,Is Normalmap|O:*
F|TextureVariation|Gives Texture UV variation that can be used to break up…|I:Heightmap,UVs,Variation Scale,Variation Levels,Heightmap Influence,Mask Channel,Random Rotation and Scale,Use Dither,HQ Edge Comparison|O:Shifted UVs,Raw UVs,DDX,DDY,Random Offset
F|UVCropping|Creates a cropped region to be multiplied to texture|I:Crop Bottom,Crop Left,Crop Right,Crop Top|O:*
F|Cm-to-Km|Converts between Centimeters and Kilometers|I:*|O:*
F|Km-to-Cm|Converts between Kilometers and Centimeters.|I:*|O:*
F|GetSlatePost0|Reference to slate postprocessed copy 0 of backbuffer.|I:*|O:RGB,LinearRGB,RGBA,LinearRGBA
F|GetSlatePost1|Reference to slate postprocessed copy 1 of backbuffer.|I:*|O:RGB,LinearRGB,RGBA,LinearRGBA
F|GetSlatePost2|Reference to slate postprocessed copy 2 of backbuffer.|I:*|O:RGB,LinearRGB,RGBA,LinearRGBA
F|GetSlatePost3|Reference to slate postprocessed copy 3 of backbuffer.|I:*|O:RGB,LinearRGB,RGBA,LinearRGBA
F|GetSlatePost4|Reference to slate postprocessed copy 4 of backbuffer.|I:*|O:RGB,LinearRGB,RGBA,LinearRGBA
F|GetUserInterfaceUV|Provides access to various built in UV sets for UI mate…|I:-|O:9-Slice UV,Pixel Size,Normalized UV,Tiling,9-Slice UV (No Tiling)
F|OctahedronToUnitVector|Unpacks a v2 Octahedron to a v3 vector.|I:*|O:*
F|UnitVectorToOctahedron|Packs a v3 vector to a v2 Octahedron.|I:*|O:*
F|Gravity_WPO|Find the velocity and updated position of an object tha…|I:Fall Start Time,Gravitational Acceleration,Current Time|O:Offset From Start Position,Instantaneous Velocity
F|Sprite_Capsule|The material function performs a number of functions to…|I:Particle Position,Capsule Diameter,Capsule Pivot Alignment,Normalized Particle Direction,Scale Along Velocity Vector,---------Scale Over Velocity Parameters---------,Particle Speed,Minimum Speed,Max Speed,Minimum Scale Factor,Maximum Scale Factor,---------- Advanced -----------,Cap Size Multiplier,Use Camera Offset,Use Advanced Features,World Position to Negate|O:Front Face Mask,Opacity Mask,World Space Normals,World Position Offset,Pixel Depth Offset,Texture Coordinates,Scale Factor
F|Sprite_Ellipsoid|The material function will align a particle, or plane,…|I:Particle Position,Particle Direction,Particle Size,Normals,Opacity Mask,World Position to Negate,Scale Along Velocity Vector,---------Scale Over Velocity Parameters---------,Particle Speed,Minimum Speed,Max Speed,Minimum Scale Factor,Maximum Scale Factor|O:Opacity Mask,World Space Normal,World Position Offset
F|Sprite_TearDrop|Stretch a particle out along the velocity vector when i…|I:Max Stretch Factor,Min Tear Drop Width,Minimum Speed,Max Speed,------ Particle Defaults Below ------,Particle Direction,Particle Position,Particle Size,Particle Speed,UV Add|O:Opacity Mask,World Space Normals,World Position Offset,Texture Coordinates
F|ManualWorldToScreenUVsTransform|This function will allow one to manually recreate any p…|I:Camera Relative Position,X Camera to World Vector,Y Camera to World Vector,Z Camera to World Vector,Tan(FOV/2)*[1,Screen Res Y/X]|O:*