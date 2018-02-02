'''
Created on Nov 4, 2014

@author: Srinivas
Contributor:  SHRISTIKA YADAV
'''
from numpy import array, int16, int32 

class simpleShape(object):
    '''
    classdocs
    '''
    points = []
    elements = []
    normals = []
    uv = []
    colors = []
    nverts = 0    
    
    

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def addTriangle(self,x0,y0,z0,x1,y1,z1,x2,y2,z2):
        
        self.points.append(x0)
        self.points.append(y0)
        self.points.append(z0)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1
        
        self.points.append(x1)
        self.points.append(y1)
        self.points.append(z1)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1
        
        self.points.append(x2)
        self.points.append(y2)
        self.points.append(z2)
        self.points.append(1.0)
        self.elements.append(self.nverts)
        self.nverts += 1
    
    def addTriangleWithNorms (self, x0,y0,z0,x1,y1,z1,x2,y2,z2, nx0,ny0,nz0,nx1,ny1,nz1,nx2,ny2,nz2 ) :
        self.points.append( x0 )
        self.points.append( y0 )
        self.points.append( z0 )
        self.points.append( 1.0 )
    
        self.normals.append( nx0 )
        self.normals.append( ny0 )
        self.normals.append( nz0 )
    
        self.points.append( x1 )
        self.points.append( y1 )
        self.points.append( z1 )
        self.points.append( 1.0 )
    
        self.normals.append( nx1 )
        self.normals.append( ny1 )
        self.normals.append( nz1 )
    
        self.points.append( x2 )
        self.points.append( y2 )
        self.points.append( z2 )
        self.points.append( 1.0 )
    
        self.normals.append( nx2 )
        self.normals.append( ny2 )
        self.normals.append( nz2 )
    
        self.nverts += 3  # three vertices per triangle
    
    
    def addTriangleWithUV (self, x0,y0,z0,x1,y1,z1,x2,y2,z2, u0, v0, u1, v1, u2, v2  ) :

        # calculate the normal
        ux = x1 - x0;
        uy = y1 - y0;
        uz = z1 - z0;
    
        vx = x2 - x0;
        vy = y2 - y0;
        vz = z2 - z0;

        nnx = (uy * vz) - (uz * vy)
        nny = (uz * vx) - (ux * vz)
        nnz = (ux * vy) - (uy * vx)
    
        # Attach the normal to all 3 vertices
        self.addTriangleWithNorms( x0,y0,z0,x1,y1,z1,x2,y2,z2, nnx, nny, nnz, nnx, nny, nnz, nnx, nny, nnz)
    
        # Attach the texture coordinates
        self.uv.append( u0 )
        self.uv.append( v0 )
        self.uv.append( u1 )
        self.uv.append( v1 )
        self.uv.append( u2 )
        self.uv.append( v2 )

        
    def clear(self):
        self.nverts= 0
        self.points = []
        self.elements = []
        self.normals = []
        self.uv = []
        self.colors = []
    
    def getVertices(self):
        return array(self.points, dtype ='float32')
    
    def getNormals(self):
        return array(self.normals, dtype ='float32')
    
    def getColors(self):
        return array(self.colors, dtype ='float32')
    
    def getUV(self):
        return array(self.uv, dtype ='float32')
        
    def getElements(self):
        return array(self.elements, dtype = 'int16')
        
    def getNVerts(self):
        return int32(self.nverts)
            
