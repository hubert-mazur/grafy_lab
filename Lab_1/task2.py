#!/usr/bin/python3.7

import sys
import math
import networkx as nx
import matplotlib.pyplot as plt

nodes_number = int(sys.argv[1])
radius = float(sys.argv[2])
alpha = 2*math.pi / nodes_number

x_0 = 20
y_0 = 20

positions = {}

for i in range(nodes_number + 1):
    positions.update({i:(x_0 + radius*math.cos(i*alpha), y_0 + radius*math.sin(i*alpha))})


adjacency = [(i+1,(i+1)%(nodes_number) + 1) for i in range(nodes_number)]
print (adjacency)
G = nx.Graph()
G.add_nodes_from([i for i in range(nodes_number)])
G.add_edges_from(adjacency)
# print (G.nodes)
plt.subplot(121).axis('off')
plt.tight_layout()
nx.draw_networkx_nodes(G,positions)
nx.draw_networkx_edges(G,positions)
nx.draw_networkx_labels(G,positions, with_labels=True)

plt.show()