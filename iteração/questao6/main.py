l = int(input())
currentL = l
km=0
while True:
    event = int(input())
    if (event == -1 and currentL>=0) or currentL<=0:
      print('Lar Deivis lar' if event == -1 and currentL>=0 else km )
      break
    if event == 0: currentL = currentL - 1
    elif event == 1: currentL = currentL + min(int(input()),l - currentL)
    elif event == 2: currentL = currentL - int(input())
    if currentL>=0: km += 1
      
     km_r = 0
test = 0
capacidade = int(input())
litros_a = capacidade
while litros_a > -1 and test!=1:
    opcao = int(input())
    if opcao == 0:
        litros_a -= 1
        km_r += 1
    elif opcao == 1:
        recarga = int(input())
        km_r += 1
        litros_a += recarga
        if litros_a > capacidade:
            litros_a = capacidade
    elif opcao == 2:
        obstaculos = int(input())
        litros_a -= obstaculos
        km_r += 1
    elif opcao == -1:
        test = 1
if test == 1 and litros_a > -1:
    print('Lar Deivis lar')
else:
    print(km_r-1)
