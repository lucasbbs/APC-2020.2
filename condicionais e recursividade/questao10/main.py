n = int(input())
def maravilhosos(x):
  if x == 1:
    return 1
  elif x % 2 != 0 : # caso seja impar
    print(int(3*x+1))
    return maravilhosos(3*x+1)
  else:
    print(int(x/2))
    return maravilhosos(x/2)

print(n)
maravilhosos(n)
