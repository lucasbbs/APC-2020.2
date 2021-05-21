lista = []
while True:
    n = int(input())
    if n == -1:
        break
    lista.append(n)
print(int(sum(lista)/len(lista)))

sum = 0
cnt = 0
while True:
    x = int(input())
    if x == -1:
        break
    sum += x
    cnt += 1
print(sum // cnt)
