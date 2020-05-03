from math import cos, sin, pi
import networkx as nx
import matplotlib.pyplot as plt
import tasks.lab4_task1 as t1

n = 10
mypgraph, mypegdes = t1.rand_digraph_edge_probability(n, 0.5)

radius = 8
alpha = 2*pi / n

x_0 = 20
y_0 = 20

positions = {}

for i in range(n):
    positions.update(
        {i: (x_0 + radius*cos(i*alpha), y_0 + radius*sin(i*alpha))})

print(mypgraph, mypegdes)
graphP = nx.DiGraph()
for i, item in enumerate(positions):
    graphP.add_node(i, pos=item)
graphP.add_edges_from(mypegdes)
labels = nx.get_edge_attributes(graphP, 'weight')
nx.draw(graphP, pos=positions)
nx.draw_networkx_labels(graphP, pos=positions)
nx.draw_networkx_edge_labels(graphP, pos=positions, edge_labels=labels, font_color='red')
plt.show()
