from math import cos, sin, pi
import networkx as nx
import matplotlib.pyplot as plt
import tasks.lab3_task1 as t1

n = 10
mylgraph, mylegdes = t1.random_weighted_graph(n, 20)
radius = 8
alpha = 2*pi / n

x_0 = 20
y_0 = 20

positions = {}

for i in range(n):
    positions.update(
        {i: (x_0 + radius*cos(i*alpha), y_0 + radius*sin(i*alpha))})

print(mylegdes)
graphR = nx.Graph()
for i, item in enumerate(positions):
    graphR.add_node(i, pos=item)
graphR.add_edges_from(mylegdes)
labels = nx.get_edge_attributes(graphR, 'weight')
nx.draw(graphR, pos=positions)
nx.draw_networkx_labels(graphR, pos=positions)
nx.draw_networkx_edge_labels(graphR, pos=positions, edge_labels=labels, font_color='red')
plt.show()
