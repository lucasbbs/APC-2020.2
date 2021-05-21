numbers = input()
last1, last0, has7_1, has7_0 = False, False, False, False
count0, count1 = 0, 0
for n in numbers:
  if n == "1":
    if last1 == True:
      count1 += 1
      if count1 >= 7: has7_1 = True
    else:
      count1 = 1
      last1 = True
      last0 = False
  elif n == "0": 
    if last0 == True:
      count0 += 1
      if count0 >= 7: has7_0 = True
    else:
      count0 = 1
      last0 = True
      last1 = False
if not has7_1 and not has7_0: print('BORA UM VIRTUAL NO CODEFORCES')
if has7_1 and not has7_0: print('VAMO TRICOLOR')
if has7_0 and not has7_1: print('VAI TIMAO')
if has7_0 and has7_1: print('JOGO PESADO')
  
  
s = input()

cnt = [0, 0]
f = [False, False]

prev = -1
for c in s:
    cur = ord(c)-ord('0')
    if cur != prev:
        cnt = [0, 0]

    prev = cur
    cnt[cur] += 1

    for i in range(2):
        if cnt[i] >= 7:
            f[i] = True

if f[0] and f[1]:
    print("JOGO PESADO")
elif f[0]:
    print("VAI TIMAO")
elif f[1]:
    print("VAMO TRICOLOR")
else:
    print("BORA UM VIRTUAL NO CODEFORCES")
    
# Solucao alternativa: Vinicius

#campo = input()

#players_cor = 0 # caractere 0
#players_spfc = 0 #caractere 1
#flagspfc = False
#flagcor = True
#sitcor = 0
#sitspfc = 0

#for i in range(0,len(campo)):
#  if campo[i] == '0':
#    if flagcor == False:
#      flagcor=True
#      flagspfc = False
#      players_spfc = max(players_spfc,sitspfc)
#      sitspfc = 0
#    sitcor = sitcor+1
#  else:
#    if flagspfc == False:
#      flagspfc=True
#      flagcor = False
#      players_cor = max(players_cor,sitcor)
#      sitcor = 0
#    sitspfc=sitspfc+1

#players_cor = max(players_cor,sitcor)
#players_spfc = max(players_spfc,sitspfc)

#if players_cor >= 7 and players_spfc >= 7:
#    print("JOGO PESADO")
#elif players_cor >= 7:
#    print("VAI TIMAO")
#elif players_spfc >= 7:
#    print("VAMO TRICOLOR")
#else:
#    print("BORA UM VIRTUAL NO CODEFORCES")
