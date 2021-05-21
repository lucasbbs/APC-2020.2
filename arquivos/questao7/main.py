p,c,filename = input().split()
c = int(c)
with open(filename) as f:
  lines = [line.strip() for line in f]

found = False
lines2=[]
for i, line in enumerate(lines):
    if p in line:
        lines2.append(i+1)
        
if lines2 != []:
    for i,line in enumerate(lines2):
        print(f'\n{filename}: {line}' if i != 0 and i == len(lines2)-1 else f'{filename}: {line}')
        for each in range(-c+line-1, c+line):
            if each < 0 or each > len(lines)-1 : pass
            else: print(lines[each])
