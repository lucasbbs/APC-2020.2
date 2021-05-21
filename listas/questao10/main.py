import itertools
stuff = list(map(int, input().split()))
N = int(input())
result = False
for L in range(0, len(stuff)+1):
  if result == True:
    break
  for subset in itertools.combinations(stuff, L):
    if sum(subset) == N:
      print("E possivel ganhar.")
      result = True
      break
if result == False: print('Impossivel ganhar.')

def verifica(n, premio):
    if premio == 0:
        return True
    elif (n < 0) or (premio < 0):
        return False
    else:
        t1 = verifica(n - 1, premio - valores[n])
        t2 = verifica(n - 1, premio)
    return t1 or t2
valores = [int(s) for s in input().split()]
premio = int(input())
if verifica(len(valores)-1, premio) == True:
    print('E possivel ganhar.')
else: 
    print('Impossivel ganhar.')
