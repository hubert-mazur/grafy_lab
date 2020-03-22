import copy


class AdjacencyList:
    def __init__(self, data):
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}
        self.nodeList = {int(i): data['list'][i][:]
                         for i in data['list'].keys()}
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}
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
                matrix[i-1][j-1] = 1
                matrix[j-1][i-1] = 1
        exportedMatrix = {}

        for i, item in enumerate(matrix):
            exportedMatrix.update({(i+1): item})

        return AdjacencyMatrix({'position': copy.deepcopy(self.positions), 'list': copy.deepcopy(exportedMatrix), 'colors': copy.deepcopy(self.colors)})

    def exportToIncidenceMatrix(self):
        incMatrix = []
        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                col = [0 for _ in range(self.numberOfNodes)]
                col[i-1] = 1
                col[j-1] = 1

                if col not in incMatrix:
                    incMatrix.append(col)

        incDict = {}
        for i, item in enumerate(incMatrix):
            incDict.update({(i+1): item})

        return IncidenceMatrix({'list': incDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})


class IncidenceMatrix:
    def __init__(self, data):
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}
        self.numberOfEdges = len(data['list'].keys())
        self.numberOfNodes = len(data['list'][list(data['list'].keys())[0]])
        self.matrix = [[0 for _ in range(self.numberOfNodes)]
                       for _ in range(self.numberOfEdges)]

        for i in data['list']:
            for j in range(self.numberOfNodes):
                self.matrix[int(i)-1][j] = data['list'][i][j]

    def prettyPrint(self):
        print('-- Incidence Matrix --', end='\n\n')

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                print(self.matrix[j][i], end=" ")
            print("")

    def exportToIncidenceMatrix(self):
        return self

    def exportToAdjacencyList(self):
        adjList = {(i+1): [] for i in range(self.numberOfNodes)}

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j+1)
            adjList[index[0]].append(index[1])
            adjList[index[1]].append(index[0])

        return AdjacencyList({'list': adjList, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})

    def exportToAdjacencyMatrix(self):
        adjMatrix = [[0 for _ in range(self.numberOfNodes)]
                     for _ in range(self.numberOfNodes)]

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j)

            adjMatrix[index[0]][index[1]] = adjMatrix[index[1]][index[0]] = 1

        adjDict = {}

        for i in range(self.numberOfNodes):
            adjDict.update({i+1: adjMatrix[i][:]})

        return AdjacencyMatrix({'list': adjDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})


class AdjacencyMatrix:
    def __init__(self, data):
        self.numberOfNodes = len(data['list'].keys())
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}

        self.matrix = [[0 for _ in range(self.numberOfNodes)]
                       for _ in range(self.numberOfNodes)]

        # indeksy w slowniku oznaczaja kolejne wiersze macierzy!
        matrixDict = data['list']

        for j in range(len(matrixDict[list(matrixDict.keys())[0]])):
            for i in matrixDict.keys():
                self.matrix[int(i)-1][j] = matrixDict[i][j]

    def prettyPrint(self):
        print('-- Adjacency Matrix --', end='\n\n')
        for i in range(self.numberOfNodes):
            for j in range(self.numberOfNodes):
                print(self.matrix[i][j], end=' ')
            print("", end="\n")

    def exportToAdjacencyMatrix(self):
        return self

    def exportToAdjacencyList(self):
        aList = {}
        nodeList = []
        for i, row in enumerate(self.matrix):
            matrixRow = row
            nodeList.clear()
            for j, item in enumerate(matrixRow):
                if item:
                    nodeList.append(j+1)
            aList.update({(i+1): nodeList[:]})

        return AdjacencyList({'list': aList, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})

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

        for i, item in enumerate(incMatrix):
            incDict.update({i+1: item})

        return IncidenceMatrix({'list': incDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})
