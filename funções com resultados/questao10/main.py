def k_esimo(n, k):
  array = []
  for i in range(1, n+1):
    array.append(i)
  array = [number for number in array if number%2 != 0 and number != n ]+[n for n in array if n%2 == 0 ] if n %2 == 0 else [number for number in array if number%2 != 0 and number != n ]+[n for n in array if n%2 == 0 ] + [n]
  return array[k-1]
  
# def k_esimo(n,k):
#   if k <= (n+1)//2:
#     return 1 + (k-1)*2;
#   else:
#     k=k-(n+1)//2
#     return 2 + (k-1)*2;
