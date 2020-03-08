import networkx as nx
import matplotlib.pyplot as plt
import task3 as t3

n = 10
mylgraph, mylegdes = t3.Gl(n, 44)
mypgraph, mypegdes = t3.Gp(n, 0.5)
print(mylgraph)
print(mypgraph)
Gr = nx.Graph()
Gr.add_nodes_from([i for i in range(n)])
Gr.add_edges_from(mylegdes)
plt.subplot(121)
nx.draw(Gr, with_labels=True, font_weight='bold')
Gp = nx.Graph()
Gp.add_nodes_from([i for i in range(n)])
Gp.add_edges_from(mypegdes)
plt.subplot(122)
nx.draw(Gp, with_labels=True, font_weight='bold')
plt.show()