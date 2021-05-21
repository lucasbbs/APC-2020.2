from itertools import combinations
N, M = map(int, input().split())
lista = []
lista_estudantes = input().split()
for n in range(M):
  lista.append(tuple(input().split()))
sets = [set(x) for x in lista]
stable = False
while not stable:
    stable = True
    for s,t in combinations(sets, 2):
        if s & t:
            s |= t
            t ^= t
            stable = False
    sets = list(filter(None, sets))
lista.extend(sets)
for m in sorted(lista_estudantes):
  lista_amigos = [[l for l in n if l!=m] for n in [list(n) for n in lista if m in n]]
  lista_amigos = [item for sublist in lista_amigos for item in sublist]
  print(m, 'possui',len(set(lista_amigos)), 'amigos')
  
  n_alunos, n_amizades = map(int, input().split())
alunos = input().split()

amizades = dict()
for aluno in alunos:
    amizades[aluno] = dict({aluno : None}) #dicionário de dicionários

for _ in range(n_amizades):
    amigo1, amigo2 = input().split()
    amizades[amigo1].update(amizades[amigo2]) #bota as chaves de amizades[amigo2] que não estão em amizades[amigo1]
    for aluno in amizades[amigo1]:
        amizades[amigo1].update(amizades[aluno]) #o circulo de amizade de a1 é atualizado
    for aluno in amizades[amigo1]:
        amizades[aluno] = amizades[amigo1] #quem era amigo de a1 (ou a2) tem seu círculo atualizado

for aluno in sorted(alunos):
    print(aluno + f' possui {len(amizades[aluno]) - 1} amigos')
    
  
