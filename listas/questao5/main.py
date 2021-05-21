valores_calculados = {0: 0, 1: 1}
N = int(input())
call = [0]*(N+1)
def fibonacci(n):
  if n in valores_calculados:
    return valores_calculados[n]
  else:
    novoValor = fibonacci(n-1)+ fibonacci(n-2)
    valores_calculados[n] = novoValor
    return novoValor
for i in range(N+1):
  if i == N:print(f'Termo: {fibonacci(i)}')
  else:fibonacci(i)

def recur_fibo(n):
  call[n] += 1
  if n <= 1:
    return n,call
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))
fibonacci(N)
print('Quantidades:')
for i, n in enumerate(recur_fibo(N)[1]):
  print(f'fibonacci({i}) - {n}')

  
quantidade = [0] * 31
def fibonacci(n):
    quantidade[n] += 1;
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

print(f'Termo: {fibonacci(n)}\nQuantidades:')
for i in range(n+1):
    print(f'fibonacci({i}) - {quantidade[i]}')
