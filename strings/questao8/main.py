N = int(input())
genomas = input()
genomasDictList = []
genomasSet = set(genomas.replace("?",""))
for gen in genomasSet:
  genomasDictList.append(dict(gen = gen, qty = genomas.count(gen)))
genomasDictList = sorted(genomasDictList, key=lambda k: k['qty'], reverse= True) 
genomasDictListFilterd = [n for n in genomasDictList if n['qty'] != genomasDictList[0]['qty']]
count =  genomas.count('?')
for n in genomasDictListFilterd:
  count, n['qty'] = count-( genomasDictList[0]['qty'] -  n['qty']), n['qty'] + genomasDictList[0]['qty'] -  n['qty']
if (all(d['qty'] == genomasDictList[0]['qty'] for d in genomasDictList) and count % 4 == 0) or (any(d['qty'] == 1 for d in genomasDictList) and count ==3 ):
  print('Segredos desvendados')
else:
  print('Feiticeiro misterioso')

  
n = int(input())
s = input()


if (n % 4) != 0:
    print("Feiticeiro misterioso")
    exit()

mx = n // 4

cnt_a = 0
cnt_c = 0
cnt_g = 0
cnt_t = 0

for c in s:
    if c == 'A':
        cnt_a += 1
    elif c == 'G':
        cnt_g += 1
    elif c == 'T':
        cnt_t += 1
    elif c == 'C':
        cnt_c += 1

if cnt_a > mx or cnt_g > mx or cnt_t > mx or cnt_c > mx:
    print("Feiticeiro misterioso")
else:
    print("Segredos desvendados")
    
#Solucao alternativa: Prof. Vinicius Borges

#n = int(input())
#genoma = input()

#ans = "Feiticeiro misterioso"

#if n % 4 == 0:
#  a=c=g=t=s=0

#  for i in range(0,n):
#    if genoma[i] == 'A':
#      a=a+1
#    elif genoma[i] == 'C':
#      c=c+1
#    elif genoma[i] == 'T':
#      t=t+1
#    elif genoma[i] == 'G':
#      g=g+1
#    else:
#      s=s+1

#  a = max(0,n//4-a)
#  c = max(0,n//4-c)
#  g = max(0,n//4-g)
#  t = max(0,n//4-t)

#  if a+c+g+t == s:
#    ans = "Segredos desvendados"

#print(ans)
