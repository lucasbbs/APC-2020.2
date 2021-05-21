n, lista = int(input()), []
while n >= 0: 
  lista.append(str(n))
  n -= 2
for i in range(len(lista)):
  print(' '.join(lista))
  lista.pop(0)
  
n = int(input())
i = n
while i >= 0:
    j = i
    while j >= 0:
        print(j, end = ' ')
        j -= 2
    print('')
    i -= 2
    
