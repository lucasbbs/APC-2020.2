navios = list(input().replace('.', ' ').split())
print(len(navios))

mapa = input()

navio = 0
tiros = 0
    
for i in range(0,len(mapa)):
  if mapa[i] == 'o':
    if navio == 0:
      navio = 1
      tiros = tiros + 1
  else:
    navio = 0
    
print(tiros)
