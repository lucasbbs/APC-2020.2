# ICPC
Um dia, os três amigos Leakim, Sarev e Odranoel decidiram fazer um time e participar de competições de programação. Os participantes geralmente recebem vários problemas durante essas competições. Bem antes do início, os amigos decidiram que só iriam implementar a solução de um problema se pelo menos dois deles tivessem certeza da solução. Caso contrário, eles não iriam escrever a solução.

Dessa forma, dado que a competição oferece n problemas aos participantes, e sabendo quais amigos tem certeza das soluções, ajude-os a encontrar o número de problemas para os quais eles vão escrever uma solução.

* Entrada
A primeira linha de entrada contém um único inteiro **1 ≤ _n_ ≤ 1000** referente ao número de problemas na competição. Depois, **_n_** linhas com três inteiros cada, sendo cada inteiro 0 ou 1. Se o primeiro número da linha é igual a 1, então Leakim tem certeza da solução, caso contrário ele não sabe. O segundo número mostra a visão de Sarev da solução e o terceiro número mostra a visão de Odranoel. Os números nas linhas são separados por espaços.

* Saída
Imprima um único inteiro indicando o número de problemas que os amigos vão implementar na competição.

* For example:

|Input|Result|
|-----|------|
|3<br>1 1 0<br>1 1 1<br>1 0 0|2|
|2<br>1 0 0<br>0 1 1|1|
|1<br>1 0 0|0|
|5<br>1 0 0<br>0 1 0<br>1 1 1<br>0 0 1<br>0 0 0|1|
|10<br>0 1 0<br>0 1 0<br>1 1 0<br>1 0 0<br>0 0 1<br>0 1 1<br>1 1 1<br>1 1 0<br>0 0 0<br>0 0 0|4|
|50<br>0 0 0<br>0 1 1<br>1 1 1<br>0 1 0<br>1 0 1<br>1 1 1<br>0 0 1<br>1 0 0<br>1 1 0<br>1 0 1<br>0 1 0<br>0 0 1<br>1 1 0<br>0 1 0<br>1 1 0<br>0 0 0<br>1 1 1<br>1 0 1<br>0 0 1<br>1 1 0<br>1 1 1<br>0 1 1<br>1 1 0<br>0 0 0<br>0 0 0<br>1 1 1<br>0 0 0<br>1 1 1<br>0 1 1<br>0 0 1<br>0 0 0<br>0 0 0<br>1 1 0<br>1 1 0<br>1 0 1<br>1 0 0<br>1 0 1<br>1 0 1<br>0 1 1<br>1 1 0<br>1 1 0<br><br>0 1 0<br>1 0 1<br>0 0 0<br>0 0 0<br>0 0 0<br>0 0 1<br>1 1 1<br>0 1 1<br>1 0 1|29|
