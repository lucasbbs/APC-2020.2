from itertools import product
N = int(input())
stuff = list( map(int, input().split()))
result = False
sum_set = list(set(map(sum, product(*[stuff, stuff]))))
for each in sum_set:
  if each == 42:
    print('sim')
    result =  True
    break
if result == False: print('nao')
 


def solve(arr):
  arr.sort()
  L = 0
  R = len(arr) - 1
  while L < R:
    if arr[L] + arr[R] == 42:
      return "sim"
    elif arr[L] + arr[R] < 42:
      L += 1
    else:
      R -= 1
  return "nao"
    
n = int(input())
nums = input().split(' ')
nums = [int(x) for x in nums]
print(solve(nums))


'''
Existem 3 formas de resolver esse problema.

A primeira, e mais óbvia, é tentar todas as somas possíveis entre 2 números do vetor, e se alguma der 42, respondemos sim. Se testamos todas as somas e nenhuma deu 42, a resposta é nao. Essa forma é simples de ser implementada, mas é pouco eficiente.

Uma segunda alternativa é ordenar o vetor. Feito isso, podemos utilizar uma técnica chamada two pointers para descobrir se é possível somar 2 números até 42 da seguinte maneira:

1. Ordenar o vetor

2. Inicializar um ponteiro L=0 e R=n−1 (primeiro e último elementos do vetor

3. Enquanto o ponteiro L for menor do que R, analisamos a soma atual. Se ela for 42, retornamos sim. Se ela for menor do que 42, então precisamos de números maiores na soma, logo incrementamos L uma posição. Se a soma for maior que 42, precisamos de números menores, logo decrementamos R uma posição.

4. Se L==R e não achamos uma soma que dá 42, podemos responder nao.



A terceira maneira de responder a questão envolve usar um mapa para armazenar quais números foram vistos. Quando você aprender sobre dicionários em Python pode tentar resolver essa questão novamente usando eles :D '''
