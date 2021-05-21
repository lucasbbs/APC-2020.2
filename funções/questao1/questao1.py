a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())
a5, b5 = map(int, input().split())

def maiorAB(a,b):
    if a > b:
        return a
    else:
        return b

print(maiorAB(a1,b1))
print(maiorAB(a2,b2))
print(maiorAB(a3,b3))
print(maiorAB(a4,b4))
print(maiorAB(a5,b5))
