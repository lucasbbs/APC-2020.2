N = int(input())
lista = []
for n in range(N):
  word, translation = input().split(None, 1)
  lista.append({word:translation})
frase = input().split()
nova_frase = ""
nova_lista = []
for palavra in frase:
    for dicts in lista:
      if palavra == list(dicts.keys())[0]:nova_lista.append(dicts[list(dicts.keys())[0]])
print(" ".join(nova_lista))
