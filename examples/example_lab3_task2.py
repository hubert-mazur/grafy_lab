#!/usr/bin/python3.7

from tasks.lab3_task2 import lab3_task2
from tasks.lab3_task3 import lab3_task3
from tasks.lab3_task4 import graphCenter
from utils.dijkstra import findPath as path
import networkx as nx
import matplotlib.pyplot as plt

numberOfNodes = 8
numberOfEdges = 19
startNode = 0

shortestPaths = lab3_task2(numberOfNodes, numberOfEdges, startNode)

for i, j in shortestPaths[2][0].items():
    print(f'{startNode} -> {i} : {j}, {path(shortestPaths[2][1], i)}')

matrix = lab3_task3(shortestPaths)

print("Macierz odleglosci:")

for i in matrix:
    for j in i:
        print(j, end='  ')
    print('')

print('\n\n')
gCenter, minimax = graphCenter(matrix)
print(f'Centrum grafu: {gCenter}, minimax: {minimax}')

# plt.subplot(111)
plt.axis('off')
G = nx.from_dict_of_lists(shortestPaths[0].nodeList)
layout = nx.spiral_layout(G, 1000)
nx.draw(G, layout)
nx.draw_networkx_labels(G, layout)
nx.draw_networkx_edge_labels(G, layout, shortestPaths[1])
plt.show()
