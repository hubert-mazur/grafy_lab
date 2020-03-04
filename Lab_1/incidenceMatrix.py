import adjacencyMatrix
import adjacencyList


class IncidenceMatrix:

    def __init__(self, data):
        self.positions = data['position']
        
        self.colors = data['colors']
        self.numberOfEdges = len(data['list'].keys())
        self.numberOfNodes = len(data['list']['1'])

        self.matrix = [[ 0 for _ in range(self.numberOfNodes)] for _ in range(self.numberOfEdges)]

        for i in range(self.numberOfEdges):
            for j in range(self.numberOfNodes):
                self.matrix[i][j] = data['list'][str(i+1)][j]

    def prettyPrint(self):        
        print('-- Incidence Matrix --', end='\n\n')

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                print(self.matrix[j][i], end=" ")
            print("")

    def exportToAdjacencyList(self):
        adjList = {(i+1): [] for i in range(self.numberOfNodes)}

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j+1)
            adjList[index[0]].append(index[1])
            adjList[index[1]].append(index[0])

        return adjacencyList.AdjacencyList({'list': adjList, 'position': self.positions, 'colors': self.colors})

    def exportToAdjacencyMatrix(self):
        adjMatrix = [[ 0 for _ in range(self.numberOfNodes)] for _ in range(self.numberOfNodes)]

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j)
            
            adjMatrix[index[0]][index[1]] = adjMatrix[index[1]][index[0]] = 1

        adjDict = {}

        for i in range(self.numberOfNodes):
            adjDict.update({str(i+1):adjMatrix[i][:]})
        
        return adjacencyMatrix.AdjacencyMatrix({'list': adjDict, 'position': self.positions, 'colors': self.colors})
