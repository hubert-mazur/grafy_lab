
from tasks.lab4_task4 import lab4_task4
from tasks.lab4_task3 import print_graph


n = 5

gTup, D = lab4_task4(n)

print('     ' + '  '.join(map(str, range(n))))
for i in range(n):
    print(f'{i} :', end='')
    for value in D[i]:
        print('{:3}'.format(value), end='')
    print()

print()
for i in range(n):
    print(i, ' : ', end='')
    print(D[i])
print_graph(gTup, n)
