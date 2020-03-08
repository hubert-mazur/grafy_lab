#!/usr/bin/python3.7

import adjacencyList
import incidenceMatrix

class AdjacencyMatrix:

    def __init__(self, data):
        self.numberOfNodes = len(data['list'].keys())
        self.positions = data['position']
        self.colors = data['colors']


        self.matrix = [[0 for _ in range(self.numberOfNodes)] for _ in range(self.numberOfNodes)]

        # indeksy w slowniku oznaczaja kolejne wiersze macierzy!
        matrixDict = data['list']
        
        for j in range(len(matrixDict['1'])):
            for i in matrixDict.keys():
                self.matrix[int(i)-1][j] = matrixDict[i][j]

    def prettyPrint(self):
        print('-- Adjacency Matrix --', end='\n\n')
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

        incDict = {}

        for i in range(len(incMatrix)):
            incDict.update({str(i+1): incMatrix[i][:]})

        return incidenceMatrix.IncidenceMatrix({'list':incDict, 'position':self.positions, 'colors':self.colors})
        