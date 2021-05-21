N = int(input())
lista = list(map(int, input().split()))
lista.sort()
found = False
for i,n in enumerate(lista):
  if n>=N:
    print(i)
    found = True
    break
if found == False: print(-1)

  def chinelo(pe_do_bill, l):
    l.sort()
    i = 0
    while ((i < len(l)) and (l[i] < pe_do_bill)):
        i += 1
    if(i == len(l)):
        return -1
    else:
        return i
v = int(input())
l = [int(i) for i in input().split()]
print(chinelo(v, l))

# Solucao alternativa: Vinicius

#def numeroIdeal(chinelos,pe):
#  ans = 0
#  for i in range(0,len(chinelos)):
#    if chinelos[i] >= pe:
#      return i
#    ans = ans + 1
#  if ans == len(chinelos):
#    return -1
#bill = int(input())
#chinelos = [int(x) for x in input().split()]
#chinelos.sort()
#print(numeroIdeal(chinelos,bill))
