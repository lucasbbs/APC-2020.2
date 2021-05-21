# Digito Zero

Dado um inteiro **_x_** escreva uma função count_0s(X) que retorne quantos digitos **0** existem na representação binária de **_x_**, a partir do digito 1 mais a esquerda do número, ou seja, o bit 1 mais significativo nessa representação.

* Entrada
O único parâmetro da sua função será um inteiro **_x_** (**_x_ ≥ 0**).

* Saída
A função deve retornar o número de dígitos 0 que existem na representação binária de **_x_**.

* Observações
Submeta somente o que foi solicitado.

No primeiro exemplo de teste, a representação binária da entrada **_x_ = 6**  é **110₂**. Portanto, existe apenas um único dígito **0** antes do bit **1** mais significativo.

No segundo exemplo de teste, a representação binária da entrada **_x_ = 8** é **1000₂**. Logo, existem três dígitos **0** antes do único bit 1, que é o mais significativo..

No terceiro exemplo de teste, a representação binária da entrada **_x_ = 28** é **10100₂**. Assim, existem três bits **0** antes do bit **1** mais significativo.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print(count_1s(6))|1
print(count_1s(8))|3
print(count_1s(20))|3
print(count_1s(323))|5
print(count_1s(1024))|10
print(count_1s(1023))|0
