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

tradutor = {}
n = int(input())
for i in range(n):
    traduzir = input().split()
    tradutor[traduzir[0]] = ' '.join(traduzir[1:])
texto = input().split()
resp = ""
for palavra in texto:
    resp += tradutor[palavra]
    resp += ' '
print(resp)

# versao pythonica
#print(' '.join([traduzir[palavra] for palavra in input().split()])


# Solucao alternativa
#
# dict = {}
# for _ in range(int(input())):
#     a, b = input().split(' ', 1)
#     dict[a] = b
# frase = input().split()
# for palavra in frase:
#     print(dict[palavra], end=' ')
# print()
