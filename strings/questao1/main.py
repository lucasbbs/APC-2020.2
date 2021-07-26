N = int(input())
for n in range(N):
  row = input()
  row = row[row.find("1")::]
  row = row[::-1]
  row = row[row.find("1")::]
  print(row.count('0') if row != '0' else '0')

#n = int(input())
#for i in range(n):
#    s = input()
#    stored = 0
#    cnt = 0
#    active = False
#    for c in s:
#        if c == '1':
#            stored += cnt
#            cnt = 0
#            active = True
#        elif active:
#            cnt += 1
#    print(stored)

# Solucao alternativa: Vinicius
#n = int(input())
#while n > 0:
#  a = input()
#  temum = 0
#  ans = 0
#  bloco = 0
#  for i in range(0,len(a)):
#    if a[i] == '1':
#      if temum == 1:
#        ans = ans + bloco
#        bloco = 0
#      else:
#        temum = 1
#    else:
#      if temum == 1:
#        bloco = bloco+1
#  print(ans)
#  n=n-1
