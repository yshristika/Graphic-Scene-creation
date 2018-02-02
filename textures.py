"""
SHRISTIKA YADAV
"""
from OpenGL.GL import *
import sys, ctypes, platform
from numpy import *
import pip
from pysoil import *

class textures (object):

    # Add any global definitions and/or variables you need here.

    ##
    # This function loads texture data for the GPU.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the various shaders.
    ##



    def loadTexture( self ) :
        # load an image file directly as a new openGL texture.
        mytexture = GLuint(0)
        mytexture1 = GLuint(0)
        mytexture = SOIL_load_OGL_texture("wood.jpg",
                                          SOIL_LOAD_AUTO,
                                          SOIL_CREATE_NEW_ID,
                                          SOIL_FLAG_MIPMAPS | SOIL_FLAG_INVERT_Y | SOIL_FLAG_NTSC_SAFE_RGB | SOIL_FLAG_COMPRESS_TO_DXT)

        mytexture1 = SOIL_load_OGL_texture("wood.jpg", SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID,
                                         SOIL_FLAG_MIPMAPS | SOIL_FLAG_INVERT_Y | SOIL_FLAG_NTSC_SAFE_RGB | SOIL_FLAG_COMPRESS_TO_DXT)

        glActiveTexture(GL_TEXTURE0 + 0)
        glBindTexture(GL_TEXTURE_2D, mytexture) # bind texture

        glActiveTexture(GL_TEXTURE0 + 1)
        glBindTexture(GL_TEXTURE_2D, mytexture1)






        pass
        
        # Add your code here.
       

    ###
    # This function sets up the parameters for texture use.
    #
    # You will need to write this function, and maintain all of the values
    # needed to be sent to the various shaders.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #  parameter values are to be sent
    ###
    def setUpTexture( self, program ) :

        glUniform1i(glGetUniformLocation(program, "imgSampler1"), 0);
        glUniform1i(glGetUniformLocation(program, "imgSampler2"), 1);
        # pass
    
        # Add your code here.

