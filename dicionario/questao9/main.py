year = int(input())
while True:
  year+=1
  if len(set(str(year))) == len(str(year)):
    print(year)
    break

def is_beautiful(n):
  digits = {}
  while n > 0:
    d = n % 10
    if d not in digits:
      digits[d] = 0

    digits[d] += 1
    if digits[d] > 1:
      return False
    n = n // 10

  return True

n = int(input()) + 1
while True:
  if is_beautiful(n):
    print(n)
    exit(0)
  n += 1

#Solucao Vinicius
#anoint = int(input())+1

#dicionario = dict()

#flag = False

#while flag == False:

#  ano = str(anoint)
#  flag = True

#  for i in range(0,10):
#    dicionario[i] = 0

#  for i in range(0,len(ano)):
#    digit = ord(ano[i])-48
#    dicionario[digit] = dicionario[digit]+1
    
#    if dicionario[digit] > 1:
#      flag = False

#  if flag == False:
#    anoint=anoint+1

#print(anoint)
