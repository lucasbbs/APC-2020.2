from itertools import product
N = int(input())
stuff = list( map(int, input().split()))
result = False
sum_set = list(set(map(sum, product(*[stuff, stuff]))))
for each in sum_set:
  if each == 42:
    print('sim')
    result =  True
    break
if result == False: print('nao')
 


def solve(arr):
  arr.sort()
  L = 0
  R = len(arr) - 1
  while L < R:
    if arr[L] + arr[R] == 42:
      return "sim"
    elif arr[L] + arr[R] < 42:
      L += 1
    else:
      R -= 1
  return "nao"
    
n = int(input())
nums = input().split(' ')
nums = [int(x) for x in nums]
print(solve(nums))
