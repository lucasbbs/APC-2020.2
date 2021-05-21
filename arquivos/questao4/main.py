strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def shifttext(shift, inp):
    data = []
    for i in inp:
      data.append(strs[(strs.index(i) - shift) % 26])    
    output = ''.join(data)
    return output

with open(input()) as f:
  lines = [line.strip() for line in f]

for i in range(int((len(lines)-1)/2)+1):
  res = ''
  pos = int(lines[2*i])
  for c in lines[2*i+1]:
    codcd = ord(c) - pos
    if codcd < ord(' '):
      codcd += 32

    res += chr(codcd)
  print(res)
