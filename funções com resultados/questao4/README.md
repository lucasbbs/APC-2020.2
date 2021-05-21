# Sequência
Observe a sequência numérica abaixo.

**1,0,2,−1,3,−2,4,...**

Sua tarefa nesse exercício será criar uma função next, que recebe 2 argumentos, **_aᵢ_** e **_i_**, respectivamente o valor do iésimo número da sequência, e seu índice i (o primeiro elemento tem índice 1. O resultado dessa função é o número **_aᵢ₊₁_**, o próximo número da sequência.

* Entrada
A entrada consiste nos parâmetros da função next, que são os dois números inteiros, **_aᵢ_** e **_i_** (**_i_** **< 10000**).

* Saída
Sua função deve imprimir um número inteiro, **_aᵢ₊₁_**, o próximo número da sequência.

* Observações
Submeta somente o que foi solicitado no enunciado da questão.

* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print(next(1,1))|0
print(next(-1, 4))|3
print(next(-4, 10))|6
print(next(-49, 100))|51
print(next(51, 101))|-50
print(next(17, 31))|-14
