n, salaries = int(input()), []
for i in range(n):
  salaries.append(int(input()))
  salaries = [i for i in salaries if i < 1000]
print(len(salaries)*1000 - sum(salaries))

n = int(input())
ans = 0
for i in range(n):
        x = int(input())
        ans += max(0, 1000-x)
print(ans)
