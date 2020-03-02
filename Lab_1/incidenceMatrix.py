class IncidenceMatrix:

    def __init__(self, data):
        self.positions = data['position']
        self.matrix = data['list']
        self.colors = data['colors']
        self.numberOfEdges = len(self.matrix)

    def prettyPrint(self):
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                print (self.matrix[j][i], end=" ")
            print("")

    