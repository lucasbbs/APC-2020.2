def count_0s(num):
  return binary(num,"")
  
def binary(num, string):
  if num == 0:
    return string[::-1].count("0")
  else:
    string = string + str(num % 2)
    return binary(num // 2, string)
# Para resolver o problema, deve-se realizar a conversão do número da entrada x para sua representação binária. Podemos fazer isso criando uma função recursiva, em que cada chamada deve gerar um bit de sua representação, bastando pegar o resto da divisão de x por 2 e contabilizar no resultado final (no comando return) a presença do bit 0. A chamada recursiva deve ter como argumento o quociente de x÷2 e ter como critério de parada o caso em que o x é igual a zero.
# def count_0s(x):
#     if x == 0:
#         return 1
#    elif x == 1:
#         return 0
#     else:
#         v = count_0s(x // 2)
#         if x % 2 == 0:
#             return v + 1
#         else:
#             return v
