import networkx as nx
import matplotlib.pyplot as plt
from tasks import lab5_task1 as t1

la, alle = t1.random_flow_net_v2(10)
print(la)

n = t1.getNumberOfV(la, len(la))

x_0 = 20
y_0 = 20

positions = {}

for il, l in enumerate(la):
    for iv, v in enumerate(l):
        positions.update({t1.getNumberOfV(la, il) + iv: (x_0 + il + iv%2 * 0.5, y_0 + iv)})

print(positions)

graph = nx.DiGraph()
graph.add_nodes_from(i for i in range(n))
graph.add_edges_from(alle)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw(graph, pos=positions)
nx.draw_networkx_labels(graph, pos=positions)
nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=labels, font_color='red')
plt.show()
