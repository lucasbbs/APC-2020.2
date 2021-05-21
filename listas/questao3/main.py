N = int(input())
lista  = list(map(int, input().split()))
print(" ".join([str(n-sorted(lista)[0]) for n in lista]))

n = int(input())
volta = [int(x) for x in input().split()]
menor = 301
for i in range(0,n):
  menor = min(menor,volta[i])
ans = str(volta[0]-menor)
for i in range(1,n):
  ans = ans + " " + str(volta[i]-menor)
print(ans)
