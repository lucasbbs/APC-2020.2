a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())
a3,b3 = map(int, input().split())
a4,b4 = map(int, input().split())
a5,b5 = map(int, input().split())

def trocarAB(a,b):
    return b, a

print(trocarAB(a1,b1)[0], trocarAB(a1,b1)[1])
print(trocarAB(a2,b2)[0], trocarAB(a2,b2)[1])
print(trocarAB(a3,b3)[0], trocarAB(a3,b3)[1])
print(trocarAB(a4,b4)[0], trocarAB(a4,b4)[1])
print(trocarAB(a5,b5)[0], trocarAB(a5,b5)[1])
