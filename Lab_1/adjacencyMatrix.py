#!/usr/bin/python3.7

import adjacencyList
import incidenceMatrix

class AdjacencyMatrix:

    def __init__(self, data):
        self.positions = data['position']
        self.matrix = data['list']
        self.colors = data['colors']
        self.numberOfNodes = len(self.matrix)

    def prettyPrint(self):
        for i in range(self.numberOfNodes):
            for j in range(self.numberOfNodes):
                print(self.matrix[i][j], end=' ')
            print("", end="\n")

    def exportToAdjacencyList(self):
        aList = {}
        nodeList = []
        for i in range(len(self.matrix)):
            matrixRow = self.matrix[i][:]
            nodeList.clear()
            for j in range(len(matrixRow)):
                if matrixRow[j]:
                    nodeList.append(j+1)
            aList.update({(i+1): nodeList[:]})
        return adjacencyList.AdjacencyList({'list': aList, 'position': self.positions, 'colors': self.colors})

    def exportToIncidenceMatrix(self):
        incMatrix = []
        counter = 0
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i][j]:
                    counter += 1
                    incMatrix.append([0 for _ in range(self.numberOfNodes)])
                    incMatrix[counter-1][i] = incMatrix[counter-1][j] = 1
        return incidenceMatrix.IncidenceMatrix({'list':incMatrix, 'position':self.positions, 'colors':self.colors})