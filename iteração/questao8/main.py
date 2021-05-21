n = int(input())
temp = 0
velocidades= []
for i in range(n):
  velocidade = int(input())
  if temp != velocidade:
    temp = velocidade
    velocidades.append(1)
  else:
    velocidades[len(velocidades)-1] += 1
velocidades.sort(reverse=True)
print(velocidades[0]) 

n = int(input())
ant = 0
seq = 0
ans = 0
for i in range(0,n):
  valor = int(input())
  if valor == ant:
    seq=seq+1
  else:
    ans = max(ans,seq)
    seq = 1
    ant = valor
ans = max(ans,seq)
print(ans)
