def count_0s(num):
  return binary(num,"")
  
def binary(num, string):
  if num == 0:
    return string[::-1].count("0")
  else:
    string = string + str(num % 2)
    return binary(num // 2, string)

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
