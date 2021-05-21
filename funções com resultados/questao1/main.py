def switch(x):
    return {
        'MM': 5,
        'MS': 7,
        'SS': 9
    }[x]

def nota(p1, p2, p3, s, n1, n2):
  x = switch(s)
  return (x*(p1+p2+p3) - n1*p1 -n2*p2)/p3
