"""
SHRISTIKA YADAV

"""
from OpenGL.GL import *
from numpy import *

class lighting (object):

    #
    # This function sets up the lighting, material, and shading parameters
    # for the Phong shader.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the vertex shader.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #    parameter values are to be sent
    #


    def setUpPhong( self,  program ) :
        if program == 8:
            Diffuse_color = [0.640000, 0.640000, 0.640000,1.0]
            Diffuse_reflection_coefficient = 0.64
            Ambient_reflection_coefficient = 1.0
            Specular_reflection_coefficient = 0.50
        elif program == 12:
            Diffuse_color = [0.89, 0.0, 0.0, 1.0]
            Diffuse_reflection_coefficient = 0.7
            Ambient_reflection_coefficient = 0.5
            Specular_reflection_coefficient = 1.0
        Ambient_color = [1.0, 1.0, 1.0,1.0]
        Specular_color = [0.50, 0.50, 0.50]




        Specular_exponent = 96.07

        light_source_Color = [10.0, 5.0, 5.0, 5.0]
        light_source_Position = [0.0, 5.0, 2.0, 1.0]

        Ambient_light_Color = [0.5, 0.5, 0.5, 1.0]

        glUniform4fv(glGetUniformLocation(program, "lightSourceColor"),1, light_source_Color)
        glUniform4fv(glGetUniformLocation(program, "lightSourcePosition"),1, light_source_Position)
        glUniform4fv(glGetUniformLocation(program, "ambient_color"),1, Ambient_color)
        glUniform4fv(glGetUniformLocation(program, "diffuse_color"),1, Diffuse_color)
        glUniform4fv(glGetUniformLocation(program, "specular_color"),1, Specular_color)
        glUniform4fv(glGetUniformLocation(program, "ambientLightColor"), 1, Ambient_light_Color)

        glUniform1f(glGetUniformLocation(program, "ambient_reflection_coefficient"),Ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "diffuse_reflection_coefficient"),Diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_reflection_coefficient"),Specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_exponent"),Specular_exponent)
        pass

        # Add your code here
        
