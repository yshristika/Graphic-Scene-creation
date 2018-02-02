"""
SHRISTIKA YADAV
"""
from OpenGL.GL import *
from numpy import *

class viewParams(object):

    # current values for transformations
    rotateDefault    = [ 0.0, 50.0, 90.0 ]
    translateDefault = [ 1.0, 0.0, -1.0 ]
    scaleDefault     = [ 1.0, 4.0, 1.0 ]

    # current view values
    eyeDefault  = [ 0.0, 3.0, 3.0 ]
    lookDefault = [ 1.0, 0.0, 0.0 ]
    upDefault   = [ 0.0, 1.0, 0.0 ]

    # clipping window boundaries
    cwLeft   = -1.0
    cwRight  = 1.0
    cwTop    = 1.0
    cwBottom = -1.0
    cwNear   = 3.0
    cwFar    = 100.5

    ###
    # This function sets up the view and projection parameter for a frustum
    # projection of the scene.
    #
    # @param program - The ID of an OpenGL (GLSL) shader program to which
    #    parameter values are to be sent
    #
    def setUpFrustum( self, program ) :
    
        leftLoc = glGetUniformLocation( program, "left" )
        rightLoc = glGetUniformLocation( program, "right" )
        topLoc = glGetUniformLocation( program, "top" )
        bottomLoc = glGetUniformLocation( program, "bottom" )
        nearLoc = glGetUniformLocation( program, "near" )
        farLoc = glGetUniformLocation( program, "far" )

        type = glGetUniformLocation(program, "type")


    
        glUniform1f( leftLoc,   self.cwLeft )
        glUniform1f( rightLoc,  self.cwRight )
        glUniform1f( topLoc,    self.cwTop )
        glUniform1f( bottomLoc, self.cwBottom )
        glUniform1f( nearLoc,   self.cwNear )
        glUniform1f( farLoc,    self.cwFar )

        glUniform1i(type, 1)

    def setUpOrtho(self, program):
        leftLoc = glGetUniformLocation(program, "left")
        rightLoc = glGetUniformLocation(program, "right")
        topLoc = glGetUniformLocation(program, "top")
        bottomLoc = glGetUniformLocation(program, "bottom")
        nearLoc = glGetUniformLocation(program, "near")
        farLoc = glGetUniformLocation(program, "far")

        type = glGetUniformLocation(program, "type")

        glUniform1f(leftLoc, self.cwLeft)
        glUniform1f(rightLoc, self.cwRight)
        glUniform1f(topLoc, self.cwTop)
        glUniform1f(bottomLoc, self.cwBottom)
        glUniform1f(nearLoc, self.cwNear)
        glUniform1f(farLoc, self.cwFar)

        glUniform1i(type, 2)

    ###
    ## This function clears any transformations, setting the values to the
    ## defaults: scale by 4 in Y, rotate by 50 in Y and 90 in Z, and
    ## translate by 1 in X and -1 in Z.
    ##
    ## @param program - The ID of an OpenGL (GLSL) shader program to which
    ##   parameter values are to be sent
    ###
    def clearTransforms( self, program ) :

        # reset the shader using global data
        thetaLoc = glGetUniformLocation( program, "theta" )
        transLoc = glGetUniformLocation( program, "trans" )
        scaleLoc = glGetUniformLocation( program, "scale" )
    
        glUniform3fv( thetaLoc, 1, self.rotateDefault )
        glUniform3fv( transLoc, 1, self.translateDefault )
        glUniform3fv( scaleLoc, 1, self.scaleDefault )


    ###
    ## This function sets up the transformation parameters for the vertices
    ## of the teapot.  The order of application is specified in the driver
    ## program.
    ##
    ## @param program - The ID of an OpenGL (GLSL) shader program to which
    ##    parameter values are to be sent
    ## @param scaleX - amount of scaling along the x-axis
    ## @param scaleY - amount of scaling along the y-axis
    ## @param scaleZ - amount of scaling along the z-axis
    ## @param rotateX - angle of rotation around the x-axis, in degrees
    ## @param rotateY - angle of rotation around the y-axis, in degrees
    ## @param rotateZ - angle of rotation around the z-axis, in degrees
    ## @param translateX - amount of translation along the x axis
    ## @param translateY - amount of translation along the y axis
    ## @param translateZ - amount of translation along the z axis
    ###
    def setUpTransforms( self, program,
                        scaleX, scaleY, scaleZ,
                        rotateX, rotateY, rotateZ,
                        translateX, translateY, translateZ ) :

        scaleVec     = [ scaleX, scaleY, scaleZ ]
        rotateVec    = [ rotateX, rotateY, rotateZ ]
        translateVec = [ translateX, translateY, translateZ ]
    
        thetaLoc = glGetUniformLocation( program, "theta" )
        transLoc = glGetUniformLocation( program, "trans" )
        scaleLoc = glGetUniformLocation( program, "scale" )

        # send down to the shader
        glUniform3fv( thetaLoc, 1, rotateVec )
        glUniform3fv( transLoc, 1, translateVec )
        glUniform3fv( scaleLoc, 1, scaleVec )

    ###
    ## This function clears any changes made to camera parameters, setting the
    ## values to the defaults: eyepoint (0.0,3.0,3.0), lookat (1,0,0.0,0.0),
    ## and up vector (0.0,1.0,0.0).
    ##
    ## @param program - The ID of an OpenGL (GLSL) shader program to which
    ##    parameter values are to be sent
    ###
    def clearCamera( self, program ) :

        posLoc = glGetUniformLocation( program, "cPosition" )
        lookLoc = glGetUniformLocation( program, "cLookAt" )
        upVecLoc = glGetUniformLocation( program, "cUp" )
    
        glUniform3fv( posLoc, 1, self.eyeDefault )
        glUniform3fv( lookLoc, 1, self.lookDefault )
        glUniform3fv( upVecLoc, 1, self.upDefault )

    ###
    ## This function sets up the camera parameters controlling the viewing
    ## transformation.
    ##
    ## @param program - The ID of an OpenGL (GLSL) shader program to which
    ##    parameter values are to be sent
    ## @param eyeX - x coordinate of the camera location
    ## @param eyeY - y coordinate of the camera location
    ## @param eyeZ - z coordinate of the camera location
    ## @param lookatX - x coordinate of the lookat point
    ## @param lookatY - y coordinate of the lookat point
    ## @param lookatZ - z coordinate of the lookat point
    ## @param upX - x coordinate of the up vector
    ## @param upY - y coordinate of the up vector
    ## @param upZ - z coordinate of the up vector
    ###
    def setUpCamera( self, program,
                    eyeX, eyeY, eyeZ,
                    lookatX, lookatY, lookatZ,
                    upX, upY, upZ ) :

        eyeVec    = [ eyeX, eyeY, eyeZ ]
        lookatVec = [ lookatX, lookatY, lookatZ ]
        upVec     = [ upX, upY, upZ ]
    
        posLoc = glGetUniformLocation( program, "cPosition" )
        lookLoc = glGetUniformLocation( program, "cLookAt" )
        upVecLoc = glGetUniformLocation( program, "cUp" )
    
        # send down to the shader
        glUniform3fv( posLoc, 1, eyeVec )
        glUniform3fv( lookLoc, 1, lookatVec )
        glUniform3fv( upVecLoc, 1, upVec )
