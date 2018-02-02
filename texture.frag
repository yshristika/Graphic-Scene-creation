#version 150

// Texture mapping vertex shader
//
// Contributor:  SHRISTIKA YADAV

// INCOMING DATA

// Here is where you should add the variables you need in order
// to propogate data from the vertex shader to the fragment shader
// so that it can do the shading and texture mapping computations

// OUTGOING DATA

out vec4 finalColor;
in vec2 texCoord;

uniform sampler2D imgSampler1;
uniform sampler2D imgSampler2;

void main()
{
    if (gl_FrontFacing == true){
        finalColor = texture(imgSampler1,texCoord);
        }
    else{
    finalColor = texture(imgSampler2,texCoord);
    }
}
