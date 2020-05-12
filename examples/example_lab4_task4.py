from tasks.lab4_task4 import lab4_task4
from tasks.lab4_task3 import print_graph, bellman_ford

from utils.dijkstra import findPath

n = 5

gRep, gTup, weights, D = lab4_task4(n)

print()
print()
print('     ' + '  '.join(map(str, range(n))))
for i in range(n):
    print(f'{i} :', end='')
    for value in D[i]:
        print('{:3}'.format(value), end='')
    print()
print()
for start in range(n):
    d, p, bool = bellman_ford(gRep, weights, start)
    if bool:
        for i, j in d.items():
            print(f'{start} -> {i} : {j}, {findPath(p, i)}')
        print()

print_graph(gTup, n)
