N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def dot(v1, v2): return sum(x*y for x,y in zip(v1,v2))
print(dot(a,  b) if dot(a,b)!=0 else 'ortogonais')

def ortogonais(v1, v2):
    calc = 0
    for i in range(len(v1)):
        calc += v1[i] * v2[i]
    if(calc==0):
        print("ortogonais")
    else:
        print(calc)

#Numero de elementos que as listas terao
n = int(input())
  
#Valor dos elementos de cada lista
v1 = list(map(int,input().strip().split()))[:n]
v2 = list(map(int,input().strip().split()))[:n]

ortogonais(v1, v2)

# Solucao alternativa: Vinicius

#def innerprod(l1,l2,n):

#  soma = 0
#  for i in range(0,n):
#    soma = soma + l1[i]*l2[i]

#  return soma

#n = int(input())

#u = list(map(int,input().strip().split()))[:n]
#v = list(map(int,input().strip().split()))[:n]

#ans = innerprod(u,v,n)

#if ans == 0:
#  print("ortogonais")
#else:
#  print(ans)
