n = int(input())
def is_prime(a):
  return all(a % i for i in range(2, a)) if (a != 0 and abs(a) != 1) else False
print("Emidio" if is_prime(n) else "Faina")

x = int(input())
i = 2
prime = True
while i*i <= x and prime:
	if x % i == 0:
		prime = False
	i += 1
if prime and x > 1:
	print("Emidio")
else:
	print("Faina")
