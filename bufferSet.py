'''
Created on Oct 20, 2017 -- to match the C++ provided by wrc

@author: jmg
Contributor:  SHRISTIKA YADAV
'''
from math import cos, sin, radians
from numpy import arange,float32
from OpenGL.GL import *
from simpleShape import *
import math

class bufferSet ():
    '''
    classdocs
    '''
    # buffer handles
    vbuffer = GLuint(0)
    ebuffer = GLuint(0)
    nbuffer = GLuint(0)
    cbuffer = GLuint(0)
    tbuffer = GLuint(0)
    
    # total number of vertices
    numElements = 0
    
    # component sizes
    vSize = 0
    eSize = 0
    tSize = 0
    cSize = 0
    nSize = 0
    
    # has buffer been set up?
    bifferInit = False

    def __init__(self, params):
        '''
        Constructor
        '''
        self.initBuffer();

    # reset buffers to empty state
    def initBuffer (self) :
        self.vbuffer = GLuint(0)
        self.ebuffer = GLuint(0)
        self.cbuffer = GLuint(0)
        self.nbuffer = GLuint(0)
        self.tbuffer = GLuint(0)
        self.numElements = 0
        self.vSize = 0
        self.eSize = 0
        self.tSize = 0
        self.cSize = 0
        self.nSize = 0
        self.bufferInit = False;

    # make a vertex or array element buffer..returns id of new buffer
    def makeBuffer (self, target, data, size) :
        buffer = GLuint (0)

        glGenBuffers (1, buffer)
        glBindBuffer( target, buffer );
        glBufferData( target, size, data, GL_STATIC_DRAW );
    
        return buffer

    # creates a set of bufferes for the object passed in
    def createBuffers (self, C) :
        
        # first, reset this BufferSet
        if( self.bufferInit ) :
            #must delete the existing buffer IDs first
            glDeleteBuffers( 1, self.vbuffer)
            glDeleteBuffers( 1, self.ebuffer )
            glDeleteBuffers( 1, self.nbuffer )
            glDeleteBuffers( 1, self.cbuffer )
            glDeleteBuffers( 1, self.tbuffer )

        #clear everything out
        self.initBuffer()

        # get the vertex count
        self.numElements = C.getNVerts()
    
        # if there are no vertices, there's nothing for us to do
        if( self.numElements < 1 ) :
            return
    
        # OK, we have vertices!
        # #bytes = number of elements * 4 floats/element * bytes/float
        self.vSize = self.numElements * 4 * 4
        points = C.getVertices()
    
        # accumulate the required vertex buffer size
        vbufSize = self.vSize;
    
        # get the color data (if there is any)
        colors = C.getColors()
        if( len(colors) > 0 ) :
            self.cSize = self.numElements * 4 * 4
        
        # get the normal data (if there is any)
        normals = C.getNormals()
        if( len (normals) > 0 ) :
            self.nSize = self.numElements * 3 * 4
                
        # get the (u,v) data (if there is any)
        uv = C.getUV()
        if( len (uv) > 0 ) :
            self.tSize = self.numElements * 2 * 4

        # get the element data
        #  #bytes = number of elements * bytes/element
        self.eSize = self.numElements * 2
        elements = C.getElements()

        # first, create the connectivity data
        self.ebuffer = self.makeBuffer( GL_ELEMENT_ARRAY_BUFFER, elements, self.eSize )
    
        # next, the vertex buffer, containing vertices
        self.vbuffer = self.makeBuffer( GL_ARRAY_BUFFER, points, self.vSize )

        # add in the color data (if there is any)
        if( self.cSize > 0 ) :
            self.cbuffer = self.makeBuffer( GL_ARRAY_BUFFER, colors, self.cSize )
    
        # add in the normal data (if there is any)
        if( self.nSize > 0 ) :
            self.nbuffer = self.makeBuffer( GL_ARRAY_BUFFER, normals, self.nSize )
    
        # add in the (u,v) data (if there is any)
        if( self.tSize > 0 ) :
            self.tbuffer = self.makeBuffer( GL_ARRAY_BUFFER, uv, self.tSize )

        # finally, mark it as set up
        self.bufferInit = True;



        

