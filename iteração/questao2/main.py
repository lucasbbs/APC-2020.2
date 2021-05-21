n = int(input())
print("1 elefante incomoda muita gente...")
for i in range(1,n):
  print(f"{i+1} elefantes incomodam{', incomodam'*i} muito mais...")
  print(f"{i+1} elefantes incomodam muita gente...")
print(f"{n +1} elefantes incomodam{', incomodam'*(n)} muito mais...")



n = int(input())
print('1 elefante incomoda muita gente...')
print('2 elefantes incomodam, incomodam muito mais...')
elefantes = 2
while elefantes <= n:
    print(str(elefantes) + ' elefantes incomodam muita gente...')
    print(str(elefantes+1) + ' elefantes incomodam', end = '')
    i = 1
    while i <= elefantes:
        print(', incomodam', end = '')
        i += 1
    print(' muito mais...')
    elefantes += 1
