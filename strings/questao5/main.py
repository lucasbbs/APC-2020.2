caminho = input()
p_pos = caminho.find("P")
x_pos = caminho.find("X")
if x_pos < p_pos: x_pos, p_pos = p_pos, x_pos
if caminho[p_pos:x_pos+1].find("#") != -1:  print('Péricles esse caminho não funciona')
elif caminho[p_pos:x_pos+1].find("X") == -1:  print("Péricles, não tem tesouro")
else:  print(f'Péricles, {caminho[p_pos:x_pos+1].find("X")-caminho[p_pos:x_pos+1].find("P")} passos')

  
 
def caminho(s: str):
  p = s.find('P')
  x = s.find('X')
  if x == -1:
    return 'Péricles, não tem tesouro'
  L = min(p, x)
  R = max(p, x)
  for v in s[L:R]:
    if v == '#':
      return 'Péricles esse caminho não funciona'
  return f'Péricles, {x - p} passos'
