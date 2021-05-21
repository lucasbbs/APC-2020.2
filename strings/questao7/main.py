A, B = input().split()
print( "ta dentro!!!" if A[-len(B):len(A)] == B else "ta fora...")

A, B = list(map(str,input().split()))
if A[-len(B):] == B:
    print("ta dentro!!!")
else:
    print("ta fora...")
 
# Solução alternativa: Jeremias

# a, b = input().split()
# if a.endswith(b):
#     print('ta dentro!!!')
# else:
#     print('ta fora...')
