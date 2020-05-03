#!/usr/bin/python3.7

# najwieksza wspolna skladowa na grafie

import tasks.lab2_task3 as t3
import tasks.dataReader as reader
import networkx as nx
import matplotlib.pyplot as plt

graph = reader.readDataFromFile('testData_lab2_task3.json')
graph = graph.exportToAdjacencyList()

arr = t3.components(graph)
print(arr)

colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'black', 4: 'yellow', 5: 'orange', 6: 'violet'}

edges = {}
for i in graph.nodeList:
    for j in graph.nodeList[i]:
        if (i, j) and (j, i) not in edges.keys():
            edges.update({(i, j): colors[arr[i - 1] - 1]})

plt.subplot(121)
plt.axis('off')
G = nx.Graph()
G.add_nodes_from(graph.nodeList.keys())
G.add_edges_from(edges.keys())
pos = nx.spring_layout(G, 5)
nx.draw_networkx_edges(G, pos, edge_color=edges.values())
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
