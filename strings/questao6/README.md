# Futebol
Nunão e Levinho amam futebol e estavam assistindo um clássico brasileiro, Corinthians x São Paulo. Estudiosos como são, eles escreviam as posições dos jogadores em uma peça de papel. Para simplificar a situação, as posições eram descritas como uma string contendo apenas 0's e 1's. Um "0" corresponde a um jogador do Corinthians e um "1" corresponde a um jogador do São Paulo.

Se existem 7 jogadores de um time, um do lado do outro, então a situação é considerada favorável àquele time. Por exemplo, a situação "00100110111111101" é favorável ao São Paulo e a situação "11110111011101" não é favorável a ninguém.

Determine para qual time a situação é favorável.

* Entrada
A primeira linha de entrada contém uma palavra s - uma palavra com apenas "0"s e "1s"  com comprimento entre **1** e **100**. Existe pelo menos um jogador de cada time no campo.


* Saída
Imprima "JOGO PESADO" se a situação for favorável para os dois times, "VAI TIMAO" se a situação for favorável apenas para o Corinthians, "VAMO TRICOLOR" se a situação for favorável apenas para o São Paulo e "BORA UM VIRTUAL NO CODEFORCES" se o jogo estiver entediante e a situação não for favorável para ninguém.

* Notas

No primeiro exemplo de teste, não existem 7 jogadores em sequência de nenhum dos dois times no campo (string da entrada);

No segundo exemplo de teste, existem 7 jogadores do Corinthians em sequência (veja a sequência de zeros na strings), logo, a vantagem é do Corinthians;

* For example:

|Input|Result|
|-----|------|
|001001|BORA UM VIRTUAL NO CODEFORCES|
|1000000001|VAI TIMAO|
|00100110111111101|VAMO TRICOLOR|
|11110111111111111|VAMO TRICOLOR|
|01|BORA UM VIRTUAL NO CODEFORCES|
|1010010100000000010|VAI TIMAO|
