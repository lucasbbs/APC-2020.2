word = input()
reversedWord = input()
print('Boa Deivis!' if word[::-1] == reversedWord else 'Poxa Deivis...')

s = input()
t = input()
if s == t[::-1]:
    print("Boa Deivis!")
else:
    print("Poxa Deivis...")
    
#Solucao alternativa: Prof. Vinicius Borges
#string = input()
#cont_string = input()
#tam1 = len(string)
#tam2 = len(cont_string)
#ans = True
#if tam1 != tam2:
#  ans = False
#else:
#  i = 0
#  while i < tam1:
#    if string[i] != cont_string[tam1-i-1]:
#      ans = False
#    i=i+1
#if ans == False:
#  print("Poxa Deivis...")
#else:
#  print("Boa Deivis!")
