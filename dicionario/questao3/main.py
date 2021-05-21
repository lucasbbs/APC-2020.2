dictionary = {}
for i in range(1,int(input())+1):
  if i%2 == 0:
    dictionary[i] = i**2
  else:
    dictionary[i] = i*5
print(dictionary)

a = int(input())
d = dict()
for x in range(1,a+1):
    if(x % 2 == 0):
        d[x] = x**2
    else:
        d[x] = 5 * x
print(d)
