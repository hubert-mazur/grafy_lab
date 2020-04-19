import copy


class AdjacencyList:
    """
        Klasa reprezentujaca liste sasiedztwa
    """

    def __init__(self, data: list):
        # wczytanie pozycji wierzcholkow (opcjonalne)
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}

        # wczytanie listy sąsiedztwa, iterując po wierzchołkach; konieczne rzutowanie do int ze wzgledu na biblioteke
        # networkx
        self.nodeList = {int(i): data['list'][i][:]
                         for i in data['list'].keys()}

        # wczytanie kolorow wierzcholkow (opcjonalne)
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}

        # calkowia liczba wierzcholkow
        self.numberOfNodes = len(self.nodeList.keys())

    def prettyPrint(self) -> 'None':
        """ Funkcja wypisujaca na stdin graf w postaci listy sasiedztwa """
        print('-- Adjacency List --', end='\n\n')

        # iteracja po wierzcholkach grafu i wypisanie listy sasiadujacych z nimi wierzcholkow
        for i in self.nodeList.keys():
            print(str(i) + ': ' + str(self.nodeList[i]))

    def exportToAdjacencyList(self) -> 'AdjacencyList':
        """ Eksport do listy sasiedztwa, zwraca self"""
        return self

    def exportToAdjacencyMatrix(self) -> 'AdjacencyMatrix':
        """
         Eksport do macierzy sasiedztwa:
         Numery wierzy i numery kolumn oznaczaja wierzcholki grafu, jezeli wierzcholek {numer wiersza}
         jest sasiadem wierzcholka {numer kolumny} wowczas w macierzy na pozycji [numer wierzcholka][numer wiersza]
         wpisana jest 1, w przeciwnym wypadku: 0.

         Przykład:

         lista sasiedztwa: 1: [2, 3, 5]
                           2: [1, 3]
                           3: [1, 2, 4]
                           4: [3, 5]
                           5: [1, 4]

        macierz sasiedztwa ma postac:
                        1|  2|  3|  4|  5|
                    1|  0   1   1   0   1
                    2|  1   0   1   0   0
                    3|  1   1   0   1   0
                    4|  0   0   1   0   1
                    5|  1   0   0   1   0

        Macierz jest symetryczna wzgledem glownej diagonali

        W implementacji macierzy uzyta jest lista list, kolejne listy oznaczaja poszczegolne WIERSZE macierzy
         """

        # inicjalizacja macierzy sasiedztwa zerami
        matrix = [[0 for _ in range(self.numberOfNodes)]
                  for _ in range(self.numberOfNodes)]

        # iteracja po wierzcholkach grafu i po liscie sasiedztwa kazdego wierzcholka
        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                # wierzcholek i jest sasiadem j, wierzcholki numerowane sa od 1...n, dlatego i-1, j-1
                matrix[i - 1][j - 1] = 1

                # wierzcholek j jest sasiadem i
                matrix[j - 1][i - 1] = 1

        # postac finalna macierzy sasiedztwa, slownik wymagany przez konstruktor klasy
        exportedMatrix = {}

        # przepisanie do slownika
        for i, item in enumerate(matrix):
            exportedMatrix.update({(i + 1): item})

        return AdjacencyMatrix({'position': copy.deepcopy(self.positions), 'list': copy.deepcopy(exportedMatrix),
                                'colors': copy.deepcopy(self.colors)})

    def exportToIncidenceMatrix(self) -> 'IncidenceMatrix':
        """
        Eksport do macierzy incydencji. Kolumny macierzy incydencji oznaczaja kolejne krawedzie, natomiast numery
        wierszy wierzcholki grafu. Liczba krawedzi rowna jest sumie sasiadow wszystkich wierzchlkow podzielonej przez 2,
        ze wzgledu na to, ze wierzcholki 1 i 2 oraz 2 i 1 polaczone sa ta sama krawedzia. Jezeli dany wierzcholek
        nalezy do krawedzi, wowczas wpisana jest 1, w przeciwnym wypadku 0.

        Przykład:

         lista sasiedztwa: 1: [2, 3, 5]
                           2: [1, 3]
                           3: [1, 2, 4]
                           4: [3, 5]
                           5: [1, 4]

         liczba krawedzi: ( len([2,3,5]) + len([1,3]) + len([1,2,4]) + len([3,5]) + len([1,4]) ) /2 = 12/2 = 6

         macierz incydencji:

                                e1|  e2|  e3|  e4|  e5|  e6|
                           1|    1    1    1    0    0    0
                           2|    1    0    0    1    0    0
                           3|    0    1    0    1    1    0
                           4|    0    0    0    0    1    1
                           5|    0    0    1    0    0    1

         W implementacji macierzy uzyta jest lista list, kolejne listy oznaczaja poszczegolne KOLUMNY macierzy
        """

        incMatrix = []

        for i in self.nodeList.keys():
            for j in self.nodeList[i]:
                # inicjalizacja kolumny macierzy
                col = [0 for _ in range(self.numberOfNodes)]

                col[i - 1] = 1
                col[j - 1] = 1

                # jezeli kolumny nie ma w macierz, mozna ja dodac
                if col not in incMatrix:
                    incMatrix.append(col)

        incDict = {}
        # przepisanie do slownika
        for i, item in enumerate(incMatrix):
            incDict.update({(i + 1): item})

        return IncidenceMatrix(
            {'list': incDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})


class IncidenceMatrix:
    """
        Klasa reprezentujaca macierz incydencji.
        Kolejne listy w slowniku oznaczaja KOLUMNY macierzy incydencji
    """

    def __init__(self, data):
        # wczytanie pozycji wierzcholkow (opcjonalnie)
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}

        # wczytanie kolorow wierzcholkow (opcjonalnie)
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}

        # wczytanie liczby krawedzi
        self.numberOfEdges = len(data['list'].keys())

        # wczytanie liczby wierzchoklow
        self.numberOfNodes = len(data['list'][list(data['list'].keys())[0]])

        # inicjalizacja macierzy incydencji
        self.matrix = [[0 for _ in range(self.numberOfNodes)]
                       for _ in range(self.numberOfEdges)]

        # wczytanie macierzy incydencji
        for i in data['list']:
            for j in range(self.numberOfNodes):
                self.matrix[int(i) - 1][j] = data['list'][i][j]

    def prettyPrint(self) -> 'None':
        """ Funkcja wypisujaca na stdin graf w postaci macierzy incydencji """
        print('-- Incidence Matrix --', end='\n\n')

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                print(self.matrix[j][i], end=" ")
            print("")

    def exportToIncidenceMatrix(self) -> 'IncidenceMatrix':
        """ Export do macierzy incydencji """
        return self

    def exportToAdjacencyList(self) -> 'AdjacencyList':
        """
            Eksport do listy sasiedztwa
            W macierzy incydencji pozycje '1' w kolumnach oznaczaja przynaleznosc wierzcholka do krawedzi.
            Do dodanej krawedzi przynaleza dokladnie 2 wierzcholki, zatem sa one sasiadami.

            Przykład:

            macierz incydencji:

                                e1|  e2|  e3|  e4|  e5|  e6|
                           1|    1    1    1    0    0    0
                           2|    1    0    0    1    0    0
                           3|    0    1    0    1    1    0
                           4|    0    0    0    0    1    1
                           5|    0    0    1    0    0    1

            Z pierwszej kolumny macierzy wynika, ze wierzcholek '1' jest sasiadem wierzcholka '2' i odwrotnie,
            kontynuujac na kolejnych kolumnach otrzymana jest list sasiedztwa.

            lista sasiedztwa:

                           1: [2, 3, 5]
                           2: [1, 3]
                           3: [1, 2, 4]
                           4: [3, 5]
                           5: [1, 4]

        """
        # inicjalizacja listy sasiedztwa
        adjList = {(i + 1): [] for i in range(self.numberOfNodes)}

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j + 1)
            adjList[index[0]].append(index[1])
            adjList[index[1]].append(index[0])

        return AdjacencyList(
            {'list': adjList, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})

    def exportToAdjacencyMatrix(self) -> 'AdjacencyMatrix':
        """
            Eksport do macierzy sasiedztwa
            W macierzy incydencji pozycje '1' w kolumnach oznaczaja przynaleznosc wierzcholka do krawedzi.
            Do dodanej krawedzi przynaleza dokladnie 2 wierzcholki, zatem sa one sasiadami.

            Przykład:

            macierz incydencji:

                                e1|  e2|  e3|  e4|  e5|  e6|
                           1|    1    1    1    0    0    0
                           2|    1    0    0    1    0    0
                           3|    0    1    0    1    1    0
                           4|    0    0    0    0    1    1
                           5|    0    0    1    0    0    1

            Z pierwszej kolumny macierzy wynika, ze wierzcholek '1' jest sasiadem wierzcholka '2' i odwrotnie,
            kontynuujac na kolejnych kolumnach otrzymana jest macierz sasiedztwa

            macierz sasiedztwa:

                               1|  2|  3|  4|  5|
                           1|  0   1   1   0   1
                           2|  1   0   1   0   0
                           3|  1   1   0   1   0
                           4|  0   0   1   0   1
                           5|  1   0   0   1   0

            W implementacji macierzy uzyta jest lista list, kolejne listy oznaczaja poszczegolne WIERSZE macierzy
        """

        # inicjalizacja macierzy sasiedztwa
        adjMatrix = [[0 for _ in range(self.numberOfNodes)]
                     for _ in range(self.numberOfNodes)]

        for i in range(len(self.matrix)):
            index = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    index.append(j)

            adjMatrix[index[0]][index[1]] = adjMatrix[index[1]][index[0]] = 1

        adjDict = {}

        # przepisanie macierzy do slownika
        for i in range(self.numberOfNodes):
            adjDict.update({i + 1: adjMatrix[i][:]})

        return AdjacencyMatrix(
            {'list': adjDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})


class AdjacencyMatrix:
    """
        Eksport do macierzy sasiedztwa
        Kolejne listy w slowniku oznaczaja WIERSZE macierzy sasiedztwa
    """

    def __init__(self, data):
        # wczytanie liczby wierzcholkow
        self.numberOfNodes = len(data['list'].keys())

        # wczytanie pozycji wierzchoklow (opcjonalnie)
        self.positions = {int(i): data['position'][i][:]
                          for i in data['position']}

        # wczytanie kolorów wierzcholkow (opcjonalnie)
        self.colors = {int(i): data['colors'][i]
                       for i in data['colors'].keys()}

        # inicjalizacja macierzy sasiedztwa
        self.matrix = [[0 for _ in range(self.numberOfNodes)]
                       for _ in range(self.numberOfNodes)]

        matrixDict = data['list']

        # wczytanie macierzy incydencji
        for j in range(len(matrixDict[list(matrixDict.keys())[0]])):
            for i in matrixDict.keys():
                self.matrix[int(i) - 1][j] = matrixDict[i][j]

    def prettyPrint(self) -> 'None':
        """ Funkcja wypisujaca na stdin graf w postaci macierzy sasiedztwa """

        print('-- Adjacency Matrix --', end='\n\n')
        for i in range(self.numberOfNodes):
            for j in range(self.numberOfNodes):
                print(self.matrix[i][j], end=' ')
            print("", end="\n")

    def exportToAdjacencyMatrix(self) -> 'AdjacencyMatrix':
        """
            Eksport do macierzy sasiedztwa
        """
        return self

    def exportToAdjacencyList(self) -> 'AdjacencyList':
        """
            Eksport do listy sasiedztwa
            W macierzy sasiedztwa '1' oznacza ze wierzcholek {numer wiersza} jest sasiadem wierzcholka {numer kolumny},

            Przykład:

            macierz sasiedztwa ma postac:

                                1|  2|  3|  4|  5|
                            1|  0   1   1   0   1
                            2|  1   0   1   0   0
                            3|  1   1   0   1   0
                            4|  0   0   1   0   1
                            5|  1   0   0   1   0

            lista sasiedztwa:
                            1: [2, 3, 5]
                            2: [1, 3]
                            3: [1, 2, 4]
                            4: [3, 5]
                            5: [1, 4]

        """
        aList = {}
        nodeList = []
        # sprawdzane sa kolejne wiersze
        for i, row in enumerate(self.matrix):
            matrixRow = row
            nodeList.clear()
            # sprawdzane sa kolejne elementy czy jest '1'
            for j, item in enumerate(matrixRow):
                if item:
                    nodeList.append(j + 1)
            aList.update({(i + 1): nodeList[:]})

        return AdjacencyList(
            {'list': aList, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})

    def exportToIncidenceMatrix(self) -> 'IncidenceMatrix':
        """
            Eksport do macierzy incydencji
            W macierzy sasiedztwa '1' oznacza, ze wierzcholek {numer wiersza} jest sasiadem wierzcholka {numer kolumny},
            zatem sa sasiadami i tworza krawedz. Krawedz laczaca wierzcholek {numer wiersza}
            i wierzcholek {numer kolumny} jest ta sama krawedzia co krawedz laczaca
            wierzcholek {numer kolumny} i wierzcholek {numer wiersza}, tj.nie sa liczone dwa razy

            Macierz sasiedztwa jest symetryczna wzgledem glownej diagonali, zatem przejscie polowy macierzy -> ponad gorna diagonala
            jest wystarczajace dla stworzenia macierzy incydencji


            Przykład:

            macierz sasiedztwa:

                               1|  2|  3|  4|  5|
                           1|  0   1   1   0   1
                           2|      0   1   0   0
                           3|          0   1   0
                           4|              0   1
                           5|                  0


            Suma jedynek w przedstawionej wyzej macierzy sasiedztwa jet rowna liczbie krawedzi grafu

            macierz incydencji:

                                e1|  e2|  e3|  e4|  e5|  e6|
                           1|    1    1    1    0    0    0
                           2|    1    0    0    1    0    0
                           3|    0    1    0    1    1    0
                           4|    0    0    0    0    1    1
                           5|    0    0    1    0    0    1

        """

        incMatrix = []
        counter = 0

        # iteracja po macierzy sasiedztwa ponad diagonala
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                if self.matrix[i][j]:
                    counter += 1
                    incMatrix.append([0 for _ in range(self.numberOfNodes)])
                    incMatrix[counter - 1][i] = incMatrix[counter - 1][j] = 1

        incDict = {}

        # przepisanie do slownika
        for i, item in enumerate(incMatrix):
            incDict.update({i + 1: item})

        return IncidenceMatrix(
            {'list': incDict, 'position': copy.deepcopy(self.positions), 'colors': copy.deepcopy(self.colors)})
