# Graphic-Scene-creation
Implementation - textingMain.py

#### The 3D scene consist of 3 objects - 
1. Floor
2. Ball
3. Lamp

- The three objects are rotated together.
- Texture applied to floor which is wooden.
- Phong shading done on ball and lamp.
- Two types of transformation done on Ball and Lamp that is Frustum and Ortho and Frustum projection on Floor.

#### Three camera positions are given - 
1. Front view (Default)
     EyePoint = -0.5, 1.0, 7.5
     Lookat Up = 0.0, 1.0, 0.0
     vector = 0.0,1.0,0.0
     
2. Top view 
      EyePoint = 0.0, 8.0, 2.5
      Lookat = 0.0, 2.0, -0.7
      Up vector = 0.0,1.0,0.0
      
3. Front distant view
      EyePoint = 0.2, 3.0, 6.5
      Lookat = 0.0, 1.0, 0.0
      Up vector = 0.0,1.0,0.0
      
## Lighting Details -

Light position = 0.0, 5.0, 2.0, 1.0
Light color = 10.0, 5.0, 5.0, 5.0
Ambient coefficient = 0.5(Lamp), 1.0(Ball)
Diffuse Coefficient = 0.7(Lamp), 0.64(Ball)
Specular coefficient = 1.0(Lamp), 0.50(Ball)
Specular Exponent = 96.07
Scene ambient light = 0.5, 0.5, 0.5, 1.0

### Different controls -
Keys        Functions
1           Select Frustum Projection
2           Select Ortho projection
a           Rotate all objects
s           Stop rotation
r           Reset rotation angles
x           Set camera position to initial front view
k           Change camera position to top view
l           Change camera position to front distant
q, Q        quit

#### Notes -
Blender used to create .obj(wavefront) file for each object. It gave an objects vertices, normals, UV, Elements, Normal Indices.

Done in Python
