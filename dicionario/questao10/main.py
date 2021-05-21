N = int(input())
lista = []
for n in range(N):
  key,value = input().split(":")
  lista.append({key:value})
for dictionary in lista:
  print(dictionary)
d = {}
for dictionary in lista:
    d.update(dictionary)
print(d)

todos_dics = dict()
for i in range(a):
    um_dic = dict()
    data = input()
    temp = data.split(':') 
    um_dic[temp[0]] = temp[1]
    lista.append(um_dic)
for i in lista:
    print(i)
    todos_dics.update(i)
print(todos_dics)
