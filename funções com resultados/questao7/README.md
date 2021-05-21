# Digito Um

Dado um inteiro **_X_** escreva uma função count_1s(X) que retorne quantos digitos **1** existem na representação binária de **_X_**.

* Entrada
O único parâmetro da sua função será um inteiro **_X_** (**_X_ ≥ 0**).

* Saída
A função deve retornar o número de dígitos 1 que existem na representação binária de X.

* Observações
Submeta somente o que foi solicitado.

No primeiro exemplo de teste, **_X_ = 16** e sua representação binária é **10000₂**. Portanto, existe apenas um único dígito **1** em sua representação binária.

No segundo exemplo de teste, **_X_ = 5** e sua representação binária é **101₂**. Assim, existem dois dígitos **1** nessa representação binária.

No terceiro exemplo de teste, **_X_ = 28** e sua representação binária é **11100₂**. Por isso, a resposta é **3**.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print(count_1s(16))|1
print(count_1s(5))|2
print(count_1s(28))|3
print(count_1s(323))|4
print(count_1s(1024))|1
print(count_1s(0))|0
