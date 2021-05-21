senha = input()
if not senha.isalnum():
  print('Senha invalida.')
elif not any(x.isupper() for x in senha):
  print('Senha invalida.')
elif not any(x.islower() for x in senha):
  print('Senha invalida.')
elif not any(x.isdigit() for x in senha):
  print('Senha invalida.')
elif not 6<=len(senha)<=32:
  print('Senha invalida.')
else:
  print('Senha valida.')
  
s = input()
mi = False
ma = False
nu = False
if((len(s) > 32) or (len(s) < 6)):
    print('Senha invalida.')
else:
    for i in s:
        if(((ord(i))>64) and ((ord(i))<91)):
            ma = True
        elif(((ord(i))>96) and ((ord(i))<123)):
            mi = True
        elif(((ord(i))>47) and ((ord(i))<58)):
            nu = True
        else:
            ma = False
            break
    if(ma and mi and nu):
        print('Senha valida.')
    else:
        print('Senha invalida.')
