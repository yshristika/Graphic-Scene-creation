# LAMP
# '''
# //  lamp.py
# //
# //  Routines for tessellating a standard teapot.
# //
# //  Students should not be modifying this file.
# //
# //  @author Srini
# Contributor:  SHRISTIKA YADAV
# '''
#
from simpleShape import simpleShape

class teapot(simpleShape):
    print "enter teapot, will draw lamp"
    lampVertices = []
    lampNormals = []
    lampElements = []
    # quadUV = []
    lampNormalIndices = []
    try:
        f = open("lamp2.obj")
        n = 1
        for line in f:

            if line[:2] == "v ":
                index1 = line.split()
                lampVertices.append(round(float(index1[1]), 2))
                lampVertices.append(round(float(index1[2]), 2))
                lampVertices.append(round(float(index1[3]), 2))

            elif line[:2] == "vn":
                index1 = line.split()
                lampNormals.append(round(float(index1[1]), 2))
                lampNormals.append(round(float(index1[2]), 2))
                lampNormals.append(round(float(index1[3]), 2))


            elif line[0] == "f":
                string = line.split()
                string.pop(0)
                string1 = string[0].split('//')
                string2 = string[1].split('//')
                string3 = string[2].split('//')
                lampElements.append(int(string1[0]) - 1)
                lampElements.append(int(string2[0]) - 1)
                lampElements.append(int(string3[0]) - 1)

                lampNormalIndices.append(int(string1[1]) - 1)
                lampNormalIndices.append(int(string2[1]) - 1)
                lampNormalIndices.append(int(string3[1]) - 1)
        f.close()
    except IOError:
        print "Could not open the .obj file..."



    lampVerticesLength = len(lampVertices)
    lampNormalsLength = len(lampNormals)
    lampElementsLength = len(lampElements)
    lampNormalIndicesLength = len(lampNormalIndices)

    def makeTeapot(self):

        for i in range(0, self.lampElementsLength, 3):


            # Calculate the base indices of the three vertices
            point1 = 3 * self.lampElements[i];  # slots 0, 1, 2
            point2 = 3 * self.lampElements[i + 1];  # slots 3, 4, 5
            point3 = 3 * self.lampElements[i + 2];  # slots 6, 7, 8


            # Calculate the base indices of the three normals
            normal1 = 3 * self.lampNormalIndices[i];  # slots 0, 1, 2
            normal2 = 3 * self.lampNormalIndices[i + 1];  # slots 3, 4, 5
            normal3 = 3 * self.lampNormalIndices[i + 2];  # slots 6, 7, 8

            # add traingles with surface normals
            self.addTriangleWithNorms(self.lampVertices[point1 + 0], self.lampVertices[point1 + 1],
                                      self.lampVertices[point1 + 2], self.lampVertices[point2 + 0],
                                      self.lampVertices[point2 + 1],
                                      self.lampVertices[point2 + 2], self.lampVertices[point3 + 0],
                                      self.lampVertices[point3 + 1],
                                      self.lampVertices[point3 + 2], self.lampNormals[normal1 + 0],
                                      self.lampNormals[normal1 + 1],
                                      self.lampNormals[normal1 + 2], self.lampNormals[normal2 + 0],
                                      self.lampNormals[normal2 + 1],
                                      self.lampNormals[normal2 + 2], self.lampNormals[normal3 + 0],
                                      self.lampNormals[normal3 + 1],
                                      self.lampNormals[normal3 + 2])

    def __init__(self):
        pass