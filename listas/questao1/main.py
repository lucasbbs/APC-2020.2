lista = list(map(int, input().split()))

def bubble_sort(arr, reversed=False):
    swap_cnt = 0
    i = len(arr) - 1
    while i > 0:
        for j in range(i):
            if not reversed:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_cnt += 1
            if reversed:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_cnt += 1
        i -= 1
    return swap_cnt
print(bubble_sort(lista))


def datagrama(l):
    inversoes = 0
    for i in range(len(l)):
        for j in range(i):
            if(l[j] > l[i]):
                inversoes += 1
    
    print(inversoes)
l = [int(i) for i in input().split()]
datagrama(l)
