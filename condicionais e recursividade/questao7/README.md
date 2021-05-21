# Múltiplos
Uma operação bastante comum dados dois números a e b é saber se a é um múltiplo de b ou não. Formalmente, um inteiro a é múltiplo de um inteiro b se existe um inteiro k tal que b∗k=a.

Nesse exercício, você deve criar uma função chamada multiple , que recebe dois inteiros,  a e b. A função deve imprimir na tela "a eh multiplo de b", caso a seja multiplo de b; "b eh multiplo de a" caso b seja multiplo de a; "nao multiplos" em quaisquer outros casos. Substitua a e b pelo valor dos argumentos para imprimir. Imprima SEM as aspas. Veja os exemplos.

* Dica: Python possui o operador '%' (módulo). Ela retorna o resto da divisão inteira de um número por outro (e.g. 2 % 10 dá como resultado o resto da divisão de 2 por 10).

* Entrada

A entrada consiste nos parâmetros da função multiple, que são os dois números inteiros a e b (−10000≤a,b≤10000).

* Saída

A função deve imprimir na tela "a eh multiplo de b", caso a seja multiplo de \(b\); "b eh multiplo de a" caso b seja multiplo de a; "nao multiplos" em quaisquer outros casos. Substitua a e b pelo valor dos argumentos para imprimir. Imprima SEM as aspas.

* Observações

Nos 2 primeiros casos de teste, 6 é múltiplo de 2, então a função imprime "6 eh multiplo de 2".
No terceiro caso de teste, nem 21 é múltiplo de 22, nem 22 de 21, então a função imprime "nao multiplos".
Submeta somente o que foi solicitado.
* For example:

Input|Expected
-----|--------
multiple(2, 6)|6 eh multiplo de 2
multiple(6, 2)|6 eh multiplo de 2
multiple(21, 22)|nao multiplos
multiple(-2, 6)|6 eh multiplo de -2
multiple(-3, 41)|nao multiplos
multiple(200, 10000)|10000 eh multiplo de 200
