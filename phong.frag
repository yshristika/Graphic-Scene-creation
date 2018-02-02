#version 150

// Phong fragment shader
//
// Contributor:  Shristika Yadav

// INCOMING DATA

// Here is where you should add the variables you need in order
// to propogate data from the vertex shader to the fragment shader
// so that it can do the shading computations

// OUTGOING DATA
out vec4 finalColor;

uniform vec4 ambient_color;
uniform vec4 diffuse_color;
uniform vec4 specular_color;

uniform float ambient_reflection_coefficient;
uniform float diffuse_reflection_coefficient;
uniform float specular_reflection_coefficient;

uniform vec4 ambientLightColor;
uniform float specular_exponent;
uniform vec4 lightSourceColor;

vec3 vNorm;
vec3 light;
vec3 vPos;

in vec3 L;
in vec3 N;
in vec3 R;
in vec3 V;

out vec4 fragColor;

void main()
{
    // Replace this code with your implementation of this shader
//    finalColor = vec4( 1.0, 1.0, 1.0, 1.0 );



	// ambient
	vec4 ambient = ambient_color * ambient_reflection_coefficient * ambientLightColor;

	// diffuse
	vec4 diffuse = diffuse_color * diffuse_reflection_coefficient * (dot(N, L));
	// the vectors have been normalized so we can replace cos by dot

	// specular
	vec4 specular = specular_color * specular_reflection_coefficient * pow(max(0.0, dot(V,R)), specular_exponent);

	fragColor = ambient + diffuse  + specular * lightSourceColor ;
//	ambient +  (diffuse + specular) ;
}
