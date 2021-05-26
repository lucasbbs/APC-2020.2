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

    
    '''
    Para resolver a questão, deve-se realizar todas as combinações possíveis de brindes e verificar se o valor somado deles resulta no valor do número sorteado s. A ideia é a seguinte: suponha um conjunto B, em que vamos adicionar os brindes que resultam no valor s. Vamos testar incluir um brinde i em B, de maneira a soma dos valores dos brindes em B não ultrapassem o número sorteado s. Tal abordagem é uma versão simples do Problema da Mochila, que pode ser resolvida por meio de uma abordagem recursiva. Assim, ao analisarmos um brinde i:

se o valor do brinde i, juntamente com o valor total dos brindes em B, não ultrapassam o valor s, podemos incluir ou não o brinde i em B.
agora, se a soma dos valores do brinde (\i\) com os valores dos brindes que já estão em B ultrapassam o valor s, não podemos incluir o brinde i em B.
Pode-se então elaborar uma função recursiva que, em cada chamada, testa se esse brinde i pode ser colocado em B, sem que a soma de todos os brindes em (\B\) (incluindo o brinde i) exceda s. Em caso afirmativo, podemos realizar duas novas chamadas nessa função: para o caso em que o brinde i é colocado em B; e para o caso em que o brinde i não é colocado em B. O critério de parada das recursões se baseia na situação em que a soma dos brindes em B resulta no número (\s\).
'''
