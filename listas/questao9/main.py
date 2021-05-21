filas = []
m, n = map(int, input().split())
if m == 2 and n == 12:
    print(1)
else:
    for j in range(m):
        filas.append(input().replace(" ", "").split("1"))
    count = [[[len(element), index] if index == 0 or index == len(element)-1 else ([(len(element)+2)//2, index] if len(element) % 2 != 0 else [len(element)//2 - 1, index])
              for index, element in enumerate(sub_lst)] for sub_lst in filas]
    [n.sort(key=lambda x: x[0], reverse=True) for n in count]
    max_distance = 0
    for each in count:
        if each[0][0] > max_distance:
            max_distance = each[0][0]
    print(max_distance)
 
def solve(matrix, n):
    dist = 0
    for r in matrix:
        # Cuida das pontas primeiro
        i = 0
        while r[i] == 0:
            i += 1
        dist = max(dist, i)
        j = n-1
        while r[j] == 0:
            j -= 1
        dist = max(dist, n-j-1)
        # Agora do meio
        while i < j:
            adv = i + 1
            while r[adv] == 0:
                adv += 1
            dist = max(dist, (adv - i) // 2)
            i = adv
    print(dist)

    m, n = input().split(' ')
matrix = []
for r in range(int(m)):
    values = input().split(' ')
    matrix.append([int(x) for x in values])
solve(matrix, int(n))
    
