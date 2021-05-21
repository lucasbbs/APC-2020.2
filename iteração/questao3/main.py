n = int(input())
S = 0

def is_prime(a):
    return all(a % i for i in range(2, a)) if a != 0 and a !=abs(1) else False
import math

def is_power(a,b):
  s=math.log(a,b)
  p=round(s)
  if (b**p)==a:
    return True
  else:
    return False

def main(i):
  if is_prime(i):
    return i**2
  elif is_power(i,2):
    return len(bin(i)[2:])-1
  elif i%2==0:
    return i/2
  else:
    return i

for j in range(1,n+1):
  S += main(j)
print(int(S))

def ehPrimo(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

n = int(input())
soma = 0

for i in range(1, n+1):

    if ehPrimo(i):
        soma += i*i
    elif bin(i).count('1') == 1:
        idx = 0
        while ((1 << idx)&i) == 0:
            idx += 1
        soma += idx
    elif i%2 == 0:
        soma += i//2
    else:
        soma += i

print(soma)

# Solução alternativa: Prof. Vinicius Borges

#def ehPrimo(n):

#  if n < 2:
#    return False

#  for i in range(2,n):
#    if n % i == 0:
#      return False

#  return True

#def ehPotenciaDois(n):
  
#  while n > 1:
#    if n%2 == 1:
#      return False
#    n=n//2
  
#  return True

#def indMSB(n):

#  ind = 0
#  while n > 1:
#    ind = ind+1
#    n=n//2
#  return ind

#x = int(input())

#ans = 0
#for a in range(1,x+1):
  
#  if ehPrimo(a) == True:
#    ans = ans + a*a
#  elif ehPotenciaDois(a) == True:
#    ans = ans + indMSB(a)
#  elif a % 2 == 0:
#    ans = ans + a//2
#  else:
#    ans = ans + a

#print(ans)
