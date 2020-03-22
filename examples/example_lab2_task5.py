import networkx as nx
import matplotlib.pyplot as plt
from tasks import lab2_task5 as t5

myrep, mytup = t5.random_k_regular_graph()
print(myrep)
graph = nx.Graph()
graph.add_nodes_from(i for i in range(len(myrep)))
graph.add_edges_from(mytup)
plt.subplot(121)
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()
