# FLOOR
# '''
# //  quad.py
# //
# //  Routines for tessellating a standard quad.
# //  The quad is parallel to the XY plane with the front face
# // pointing down the +Z axis
# //
# //  Students should not be modifying this file.
# //
# //  @author Srini
# Contributor:  SHRISTIKA YADAV
# '''

from simpleShape import simpleShape

from simpleShape import simpleShape


class quad(simpleShape):
    quadVertices = []
    quadNormals = []
    quadElements = []
    quadUV = []
    normalIndices = []
    try:
        f = open("floor2.obj")
        n = 1
        for line in f:

            if line[:2] == "v ":
                index1 = line.split()
                quadVertices.append(round(float(index1[1]),2))
                quadVertices.append(round(float(index1[2]),2))
                quadVertices.append(round(float(index1[3]),2))

            elif line[:2] == "vn":
                index1 = line.split()
                quadNormals.append(round(float(index1[1]),2))
                quadNormals.append(round(float(index1[2]),2))
                quadNormals.append(round(float(index1[3]),2))


            elif line[:2] == "vt":
                index1 = line.split()
                quadUV.append(round(float(index1[1]),2))
                quadUV.append(round(float(index1[2]),2))


            elif line[0] == "f":
                string = line.split()
                string.pop(0)
                string1 =string[0].split('/')
                string2 = string[1].split('/')
                string3 = string[2].split('/')
                quadElements.append(int(string1[0])-1)
                quadElements.append(int(string2[0])-1)
                quadElements.append(int(string3[0])-1)

        f.close()
    except IOError:
        print "Could not open the .obj file..."

    quadVerticesLength = len(quadVertices)
    quadNormalsLength = len(quadNormals)
    quadElementsLength = len(quadElements)


    def makeQuad(self):
        print self.quadElementsLength
        print self.quadVerticesLength
        for i in range(0, self.quadElementsLength - 2, 3):

            # Calculate the base indices of the three vertices
            point1 = 3 * self.quadElements[i];  # slots 0, 1, 2
            point2 = 3 * self.quadElements[i + 1];  # slots 3, 4, 5
            point3 = 3 * self.quadElements[i + 2];  # slots 6, 7, 8

            # Calculate the base indices of the three texture coordinates
            normal1 = 2 * self.quadElements[i];  # slots 0, 1, 2
            normal2 = 2 * self.quadElements[i + 1];  # slots 3, 4, 5
            normal3 = 2 * self.quadElements[i + 2];  # slots 6, 7, 8

            # Add triangle and texture coordinates
            self.addTriangleWithUV(self.quadVertices[point1 + 0],
                                   self.quadVertices[point1 + 1],
                                   self.quadVertices[point1 + 2],
                                   self.quadVertices[point2 + 0],
                                   self.quadVertices[point2 + 1],
                                   self.quadVertices[point2 + 2],
                                   self.quadVertices[point3 + 0],
                                   self.quadVertices[point3 + 1],
                                   self.quadVertices[point3 + 2],
                                   self.quadUV[normal1 + 0],
                                   self.quadUV[normal1 + 1],
                                   self.quadUV[normal2 + 0],
                                   self.quadUV[normal2 + 1],
                                   self.quadUV[normal3 + 0],
                                   self.quadUV[normal3 + 1])

    def __init__(self):
        pass