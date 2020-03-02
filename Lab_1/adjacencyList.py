import adjacencyMatrix

class AdjacencyList:

    def __init__(self, data):
        self.positions = data['position']
        self.nodeList = data['list']
        self.colors = data['colors']
        self.numberOfNodes = len(self.nodeList.keys())

    def exportToAdajcencyMatrix(self):
        matrix = [[0 for _ in range(self.numberOfNodes)] for _ in range(self.numberOfNodes)]

        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                matrix[int(i)-1][j-1] = 1

        # print (matrix)
        return adjacencyMatrix.AdjacencyMatrix({'position': self.positions, 'list': matrix, 'colors': self.colors})
