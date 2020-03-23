from lab3_task5 import min_spanning_tree_Kruskal

list_of_values = [[7,2,3],[7,7,8],[8,0,7],[8,1,2],[9,3,4],[10,5,4],[11,1,7],[14,3,5],[1,7,6],[2,8,2],[2,6,5],[4,0,1],[4,2,5],[6,8,6]]
mst = min_spanning_tree_Kruskal(list_of_values, 9)

print("Printing minimum spanning tree")
for weight, source, destination in sorted(mst, key=lambda edge: edge[1]):
    print("Edge from {} to {} (weight: {})".format(source, destination, weight))
