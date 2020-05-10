from utils.bellman_ford import bellman_ford
from utils.dijkstra import findPath

from tasks.lab4_task3 import lab4_task3, print_graph


n = 5
start = 0

gTup, d, p = lab4_task3(n, start)

if isinstance(d, dict):
    # print('d : ', d)
    print()
    for i,j in d.items():
        print(f'{start} -> {i} : {j}, {findPath(p, i)}')


print_graph(gTup, n)

