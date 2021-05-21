import os
reads = input().split()
if not os.path.exists(reads[len(reads)-1]): print('nao da pra abrir')
else:
    with open(reads[len(reads)-1]) as f:
        lines = [tuple((lines.split()[0], int(lines.split()[1]))) for lines in f]
    print('da pra abrir')
    [print(tuple((lines[0], int(lines[1]))))for lines in sorted(lines, key = lambda x: x[1], reverse= True)]
