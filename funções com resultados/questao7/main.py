def count_1s(num):
  return binary(num,"")
  
def binary(num, string):
  if num == 0:
    return string[::-1].count("1")
  else:
    string = string + str(num % 2)
    return binary(num // 2, string)

  
# def count_1s(x):
#     if x == 0:
#         return 0
#     return count_1s(x // 2) + x % 2
