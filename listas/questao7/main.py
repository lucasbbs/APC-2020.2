import statistics
lista = list(map(int, input().split()))
print(f'{statistics.mean(lista):.1f}')
print(f'{statistics.pstdev(lista):.1f}')

import math
lista = [int(i) for i in input().split()]
avg = sum(lista)/len(lista)
var = sum([(i - avg)**2 for i in lista])/len(lista)
print(f'{avg:.1f}')
print(f'{math.sqrt(var):.1f}')
