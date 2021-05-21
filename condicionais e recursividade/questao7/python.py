def multiple(a, b):
    if abs(a)>abs(b):
        if a%b==0:
            print(f'{a} eh multiplo de {b}')
        else:
            print('nao multiplos')
    elif abs(a)<abs(b):
        if b%a == 0:
            print(f'{b} eh multiplo de {a}')
        else:
            print('nao multiplos')
    else:
        print(f'{b} eh multiplo de {a}')
       
#Colocar aqui a solucao
#def multiple(a, b):
#    if a % b == 0:
#        print(f'{a} eh multiplo de {b}')
#    elif b % a == 0:
#        print(f'{b} eh multiplo de {a}')
#    else:
#        print('nao multiplos')
