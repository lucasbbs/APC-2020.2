#def dinheiros(n,a,b):
#  if n == 1:
#      galoes2Litro =0
#      galoes1Litro = n
#      print(galoes2Litro*b+galoes1Litro*a)
#  else:
#    if a/b >= 1:
#      galoes2Litro = n//2
#      galoes1Litro = n - n//2*2
#      print(galoes2Litro*b+galoes1Litro*a)
#    else:
#      galoes1Litro = n
#      galoes2Litro = 0
#      print(galoes2Litro*b+galoes1Litro*a)


def dinheiros(n, a, b):
    if 2 * a <= b:
        print(n * a)
    else:
        print((n // 2) * b + (n % 2) * a)
        
