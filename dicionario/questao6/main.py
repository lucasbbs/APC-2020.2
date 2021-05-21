def stockmarket(stock):
    string = ''
    sum = 0
    dic ={}
    for n in stock:
      if n[0] != string:
        string = n[0]
        sum = 0
        sum = sum + n[1]*n[2]
        dic[string] = float(sum)
      else:
        sum = sum + n[1]*n[2]
        dic[string] = float(sum)
    return dic
  
def stockmarket(stock):
    valor = {row[0]:0.0 for row in stock}
    for row in stock:
       valor[row[0]] += row[1] * row[2]

    return valor
