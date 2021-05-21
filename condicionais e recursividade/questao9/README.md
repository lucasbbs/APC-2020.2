# Comprar água
Em Campinas, cidade do interior de São Paulo, existem infinitos galões de água de 1 litro, que custam **_a_** dinheiros, e infinitos galões de 2 litros, que custam **_b_** dinheiros, disponíveis para venda. Qual o menor número de dinheiros necessário para Fagundes comprar **exatamente** n litros de água?

Escreva uma função chamada dinheiros que recebe três parâmetros referentes ao número n de Litros desejado por Fagundes, o valor a de galões de 1L e o valor **_b_** de galões de 2L. A função deve imprimir o pedido com menor valor.

* Entrada
Os parâmetros da função são três inteiros **_n_**, **_a_**, **_b_** ≥ **1**.

* Saída 
Imprima um único inteiro com a menor quantidade de dinheiro que Fagundes precisa gastar.

* Observações
No primeiro caso de teste, Fagundes quer comprar 10 litros de água. O galão de 1 litro custa 1 dinheiros e o galão de 2 litros custa 3 dinheiros. Para comprar exatamente essa quantidade, Fagundes calculou que irá gastar no mínimo 10 dinheiros.
No segundo caso de teste, Fagundes quer comprar 7 litros de água. O galão de 1 litro custa 3 dinheiros e o galão de 2 litros custa 2 dinheiros. Para comprar exatamente essa quantidade, Fagundes calculou que irá gastar no mínimo 9 dinheiros.
No terceiro caso de teste, Fagundes quer comprar 1 litro de água. O galão de 1 litro custa 1000 dinheiros e o galão de 2 litros custa 1 dinheiro. Para comprar exatamente essa quantidade, Fagundes calculou que irá gastar no mínimo 1000 dinheiros.
Submeta somente o que foi solicitado.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
dinheiros(10, 1, 3)|10
dinheiros(7, 3, 2)|9
dinheiros(1, 1000, 1)|1000
dinheiros(3, 1, 3)|3
dinheiros(3, 3, 1)|4
dinheiros(2, 1, 1)|1
