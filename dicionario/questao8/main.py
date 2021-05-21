N = int(input())
for n in range(N):
  line = input()
  if line[0]=="R":
    operation, name = line.split()
    print(name, dic_inicial.get(name,""))
  else:
    operation, name, grade = line.split()
    dic_inicial[name] = grade
    
n = int(input())
for _ in range(n):
    l = input().split()
    if l[0] == 'R':
        print(f'{l[1]} {dic_inicial[l[1]]}')
    else:
        dic_inicial[l[1]] = l[2]
        

# Solução: Prof. Vinicius Borges
#q = int(input())

#dicionario = {
#    'João' : 10,
#    'Maria' : 10,
#    'Jorge' : 4,
#    'Marta' : 5,
#    'Mário' : 6,
#    'Mikael' : 9
#}

#for i in range(0,q):
#    
#    comands = input().split()
#    c = comands[0]
#    nome = comands[1]
#    
#    if c == 'C':
#        nota = int(comands[2])
#        dicionario[nome]=nota
#    elif c == 'R':
#        nota = dicionario[nome]
#        print(nome+" "+str(nota))
#    else:
#        nota = int(comands[2])
#        dicionario[nome]=nota
