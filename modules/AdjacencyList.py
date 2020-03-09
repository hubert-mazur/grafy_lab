import sys
import AdjacencyMatrix
import IncidenceMatrix

class AdjacencyList:

    def __init__(self, data):
        self.positions = data['position']
        self.nodeList = data['list']
        self.colors = data['colors']
        self.numberOfNodes = len(self.nodeList.keys())

    def prettyPrint(self):
        print('-- Adjacency List --', end='\n\n')

        for i in self.nodeList.keys():
            print(str(i) + ': ' + str(self.nodeList[i]))

    def exportToAdjacencyList(self):
        return self

    def exportToAdjacencyMatrix(self):
        matrix = [[0 for _ in range(self.numberOfNodes)]
                  for _ in range(self.numberOfNodes)]

        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                matrix[int(i)-1][j-1] = 1
                matrix[j-1][int(i)-1] = 1
        exportedMatrix = {}

        for i in range(len(matrix)):
            exportedMatrix.update({str(i+1):matrix[i]})

        return AdjacencyMatrix.AdjacencyMatrix({'position': self.positions, 'list': exportedMatrix, 'colors': self.colors})

    def exportToIncidenceMatrix(self):
        incMatrix = []
        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                col = [ 0 for _ in range(self.numberOfNodes)]
                col[int(i)-1] = 1
                col[j-1] = 1

                if col not in incMatrix:
                    incMatrix.append(col)

        incDict = {}
        for i in range(len(incMatrix)):
            incDict.update({str(i+1): incMatrix[i][:]})
                
        return IncidenceMatrix.IncidenceMatrix({'list': incDict, 'position': self.positions, 'colors': self.colors})

