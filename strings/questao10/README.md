# Bit++
A linguagem de programação clássica da UnBanda é a UnBit. A linguagem é peculiar e bastante complicada uma vez que só tem uma variável, chamada x e duas operações disponíveis:

Operação ++ aumenta o valor da variável **_x_** em 1.
Operação -- diminui o valor da variável **_x_** em 1.
Uma linha de código na UnBit consiste exatamente de uma operação e uma variável **_x_**. A linha é escrita sem espaços, ou seja, só pode conter os caracteres +, - e X. Executar uma linha significa aplicar a operação que está nela e executar um programa significa interpretar todas as linhas desse programa.

Você recebe um programa em UnBit. O valor inicial de **_x_** é 0. Execute o programa e descubra o valor final da variável **_x_** depois que todas as linhas são executadas.

Entrada
O número n de linhas com as respectivas instruções do programa.



Saída
Um único inteiro - o valor final de x


Observações
No caso de teste 1, o programa tem 1 linha com ++ que aumenta o valor de **_x_** em 1 (**_x_**=1). O valor final de x é 1.
No caso de teste 2, o programa tem 2 linhas. A primeira aumenta o valor de **_x_** em 1 (**_x_**=1) e a segunda diminui o valor de **_x_** em 1 (**_x_**=0). O valor final de **_x_** é 0.
No caso de teste 3, o programa tem 3 linhas. Cada linha aumenta o valor de **_x_** em 1. O valor final de **_x_** é 3.

For example:

|Input|Result|
|-----|------|
|1<br>++X|1|
|2<br>X++<br>--X|0|
|3<br>++X<br>++X<br>++X|3|
|2<br>--X<br>--X|-2|
|5<br>++X<br>--X<br>++X<br>--X<br>--X|-1|
|28<br>X--<br>++X<br>X++<br>X++<br>X++<br>--X<br>--X<br>X++<br>X--<br>++X<br>X++<br>--X<br>X--<br>X++<br>X--<br>++X<br>++X<br>X++<br>X++<br>X++<br>X++<br>--X<br>++X<br>--X<br>--X<br>--X<br>--X<br>X++|4|
