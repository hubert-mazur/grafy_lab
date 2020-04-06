import networkx as nx
import matplotlib.pyplot as plt
import tasks.lab5_task1 as t1

la, alle = t1.random_flow_net(10)
print(alle)
graph = nx.DiGraph()
graph.add_nodes_from(i for i in range(t1.getNumberOfV(la, len(la))))
graph.add_edges_from(alle)
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()