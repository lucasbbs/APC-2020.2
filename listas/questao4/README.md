# Jonathan e os outros chinelos
Jonathan achou outra caixa com mais de seus chinelos velhos em sua casa, e decidiu dar para seu irmãozinho Bill todos os pares que ainda irão caber em seus pés e doar o restante. Para escolher o chinelo, Jonathan os enfileirou em ordem crescente de tamanho em sua frente e procurou o primeiro que era do tamanho certo ou maior do que o que seu irmão atualmente calça, já que ele ainda irá crescer.

* Entrada
A primeira linha apresenta um inteiro **_T_ ( 15 ≤ _T_ ≤ 40 )**, que representa quanto Bill calça. Na segunda linha são dados **_N_ ( 1 ≤ _N_ ≤ 10 )** inteiros, separados por espaço, cada um representando o tamanho de um chinelo na caixa velha. Os chinelos estão desordenados na caixa.

* Saída
Uma linha com um inteiro que representa a posição do primeiro chinelo que cabe no pé de Bill. Caso não exista, imprima -1.

* Observação

Jonathan sempre conta seus chinelos iniciando em 0.

No primeiro caso de teste, o menor número (32) já maior ou igual ao número do calçado de Bill (30). Portanto a posição é 0.

No segundo caso de teste, o quarto maior número (38) é o primeiro que é maior ou igual ao número do calçado de Bill (34). Portanto a posição é 3.

* For example:

|Input|Result|
|-|-|
|30<br>32 40 35 37|0|
|34<br>30 38 32 28|3|
|38<br>30 35 36 32 38 39|4|
|30<br>29|-1|
|1<br>1|0|
