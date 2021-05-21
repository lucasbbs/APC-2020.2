n = int(input())
soma = 0
for n in range(n):
  if sum(list(map(int, input().split()))) >=2: soma +=1
print(soma)

n = int(input())
ans = 0
for i in range(n):
	a, b, c = [int(x) for x in input().split()]
	s = a + b + c - 1
	ans += max(0, min(1, s))
print(ans)


#solução alternativa
"""
n = int(input())
cont = 0
for i in range(1, n+1):
    sl, ss, so = map(int, input().split())
    if sl + ss + so >=2:
        cont +=1
print(cont)
"""
