# BALL
"""
Contributor:  SHRISTIKA YADAV
"""
from simpleShape import simpleShape


class ball(simpleShape):
    print "enter house, will draw ball"
    ballVertices = []
    ballNormals = []
    ballElements = []
    ballNormalIndices = []
    try:
        f = open("ball1.obj")
        n = 1
        for line in f:

            if line[:2] == "v ":
                index1 = line.split()
                ballVertices.append(round(float(index1[1]), 2))
                ballVertices.append(round(float(index1[2]), 2))
                ballVertices.append(round(float(index1[3]), 2))

            elif line[:2] == "vn":
                index1 = line.split()
                ballNormals.append(round(float(index1[1]), 2))
                ballNormals.append(round(float(index1[2]), 2))
                ballNormals.append(round(float(index1[3]), 2))

            elif line[0] == "f":

                string = line.split()
                string.pop(0)
                string1 = string[0].split('//')
                string2 = string[1].split('//')
                string3 = string[2].split('//')
                ballElements.append(int(string1[0]) - 1)
                ballElements.append(int(string2[0]) - 1)
                ballElements.append(int(string3[0]) - 1)

                ballNormalIndices.append(int(string1[1]) - 1)
                ballNormalIndices.append(int(string2[1]) - 1)
                ballNormalIndices.append(int(string3[1]) - 1)
                # print ballElements
                # print "string = ", string1, string2, string3

        f.close()
    except IOError:
        print "Could not open the .obj file..."



    lampVerticesLength = len(ballVertices)
    lampNormalsLength = len(ballNormals)
    lampElementsLength = len(ballElements)
    lampNormalIndicesLength = len(ballNormalIndices)

    def makeBall(self):


        for i in range(0, self.lampElementsLength, 3):

            # Calculate the base indices of the three vertices
            point1 = 3 * self.ballElements[i];  # slots 0, 1, 2
            point2 = 3 * self.ballElements[i + 1];  # slots 3, 4, 5
            point3 = 3 * self.ballElements[i + 2];  # slots 6, 7, 8

            # Calculate the base indices of the three normals
            normal1 = 3 * self.ballNormalIndices[i];  # slots 0, 1, 2
            normal2 =3 * self.ballNormalIndices[i + 1];  # slots 3, 4, 5
            normal3 =3 * self.ballNormalIndices[i + 2];  # slots 6, 7, 8


            # add traingles with surface normals
            self.addTriangleWithNorms(self.ballVertices[point1 + 0], self.ballVertices[point1 + 1],
                                      self.ballVertices[point1 + 2], self.ballVertices[point2 + 0],
                                      self.ballVertices[point2 + 1],
                                      self.ballVertices[point2 + 2], self.ballVertices[point3 + 0],
                                      self.ballVertices[point3 + 1],
                                      self.ballVertices[point3 + 2], self.ballNormals[normal1 + 0],
                                      self.ballNormals[normal1 + 1],
                                      self.ballNormals[normal1 + 2], self.ballNormals[normal2 + 0],
                                      self.ballNormals[normal2 + 1],
                                      self.ballNormals[normal2 + 2], self.ballNormals[normal3 + 0],
                                      self.ballNormals[normal3 + 1],
                                      self.ballNormals[normal3 + 2])

    def __init__(self):
        pass