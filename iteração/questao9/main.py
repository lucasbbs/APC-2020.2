N, lista = int(input()), []
for n in range(N):
  lista.append(int(input()))
lista.sort()
print('Menor:',lista[0])
print('Maior:',lista[len(lista)-1])

a = int(input())
menor = 1000000
maior = -1000000
i = 0
while i < a:
    n = int(input())
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i += 1
print('Menor: ' + str(menor))
print('Maior: ' + str(maior))
