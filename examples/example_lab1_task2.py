#!/usr/bin/python3.7

import math
import networkx as nx
import matplotlib.pyplot as plt
import tasks.dataReader as dataReader

nodeList = dataReader.readDataFromFile("examples/dataTask2.json")

nodes_number = nodeList.numberOfNodes
radius = 8
alpha = 2*math.pi / nodes_number

x_0 = 20
y_0 = 20

positions = {}

for i in range(1,len(nodeList.nodeList.keys())+1):
    nodeList.nodeList[int(i)] = nodeList.nodeList.pop(str(i))

for i in range(nodes_number):
    positions.update(
        {(i+1): (x_0 + radius*math.cos(i*alpha), y_0 + radius*math.sin(i*alpha))})


print(positions)
G = nx.from_dict_of_lists(nodeList.nodeList)

plt.subplot(121).axis('off')
plt.tight_layout()
print(G.nodes)
nx.draw_networkx_nodes(G, pos=positions)
nx.draw_networkx_edges(G, pos=positions)
nx.draw_networkx_labels(G, pos=positions)

plt.show()
