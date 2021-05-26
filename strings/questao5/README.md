# Tesouro
Péricles está em uma caverna, onde supostamente existe um tesouro. No entanto está muito escuro na caverna e, portanto, Péricles pediu sua ajuda para saber quantos passos ele tem que andar até o tesouro, se é que existe um. Entretanto, deve-se considerar um problema adicional: partes da caverna colapsaram, então Péricles talvez não consiga chegar até o tesouro, mesmo que ele exista.

O mapa funciona da seguinte maneira: é uma string (a caverna é bem estreita, e só da pra andar para a esquerda ou direita) composta por ' ', '#', 'P' e 'X'. O espaço em branco ' ' indica uma parte intacta da caverna, por onde Péricles pode passar; 'P' é a posição de Péricles; 'X' indica o tesouro; e '#' indica uma parte da caverna colapsada, por onde Péricles não pode passar. 

* Entrada

A entrada consiste numa string **_s_**, indicando o mapa.

* Saída

Imprima "Péricles, não tem tesouro" se não houver tesouro na caverna.

Imprima "Péricles esse caminho não funciona" se não houver um caminho que leve Péricles até o tesouro de sua posição atual.

Imprima "Péricles, **_d_** passos", onde **_d_** é o número de passos que Péricles precisa andar até o tesouro. Se for para a direita, **_d_** será um número positivo. Se for para a esquerda, **_d_** será um número negativo.

* Observações

No primeiro exemplo, Péricles está a 4 passos de distância do tesouro, e não tem nenhuma parede entre ele e o tesouro, então é possível chegar até lá;
O segundo exemplo é semelhante ao primeiro, mas Péricles tem que se mexer para a esquerda, resultando em −4 passos;
No terceiro exemplo de teste, existem partes da caverna colapsadas entre Péricles e o tesouro, então não é possível chegar até ele.

* For example:

|Input|Result|
|-----|------|
|#  P   X#|Péricles, 4 passos|
|#X   P#|Péricles, -4 passos|
|# P ##   X #|Péricles esse caminho não funciona|
|#       P   #|Péricles, não tem tesouro|
|#### P       #X##   ### # ###   #|Péricles esse caminho não funciona|
|##    ## #P              X     ## ### # # #    #|Péricles, 15 passos|
