# Dêivis em fuga!
Com sua ajuda para ganhar dinheiro com a banda, Dêivis não só conseguiu dinheiro para voltar para casa como também conseguiu passar a perna em seus amigos e usar todo o dinheiro para comprar um carro!

Agora os amigos de Dêivis estão com muita raiva dele e pretendem impedir que Dêivis volte para casa com o carro. O carro de Dêivis possui um tanque de combustível com capacidade de l litros, cada quilômetro do caminho para casa de Dêivis é descrito da seguinte forma:

0 - O carro passa normalmente por este quilômetro, gastando 1 litro de combustível.

1 - Existe um posto que enche o tanque do carro em x litros, o carro não gasta combustı́vel ao passar por este quilômetro.

2 - Existe um obstáculo colocado pelos amigos de Dêivis, que faz com que o carro gaste **_y_** litros, ao invés de 1, para passar por este quilômetro.

-1 - Dêivis chegou em casa.

Dêivis começa a fuga no primeiro quilômetro, com o tanque do carro cheio, e é obrigado a parar em um quilômetro caso este seja o da sua morada, ou caso a quantidade de litros em seu tanque não seja suficiente para passar pelo quilômetro. Caso um determinado quilômetro exija mais combustível do que a quantidade disponível Dêivis não passa este quilômetro, se a quantidade exigida for menor ou igual à quantidade de combustível disponível, ele chega ao próximo quilômetro, mesmo que com o tanque vazio. Determine quantos quilômetros ele consegue se mover até que seja obrigado a parar.

* Entrada
A primeira linha da entrada é composta por um inteiro **2 ≤ _l_ ≤ 10⁶** que representa a capacidade em litros do tanque do carro de Dêivis. Em seguida um número arbitrário de linhas, cada linha descreve um quilômetro do caminho para a casa de Dêivis, o ultimo número da entrada é sempre -1.  Caso o primeiro número de um linha que descreve o quilômetro seja 1 ou 2, o número na linha abaixo representará  **1 ≤ _x_ ≤ l** ou **2 ≤ _y_ ≤ l**, de acordo com o evento.

* Saída
Caso Dêivis consiga chegar em casa deve ser apresentada a frase "Lar Deivis lar" na saı́da. Caso contrário deve ser mostrado inteiro indicando quantos quilômetros o carro de Dêivis consegue se mover até que o tanque esvazie.

* Notas

No primeiro exemplo de teste, pode-se simular o processo, quilômetro a quilômetro, e verificando o tanque do carro, conforme a ilustração a seguir:

![](https://raw.githubusercontent.com/lucasbbs/APC-2020.2/main/itera%C3%A7%C3%A3o/questao6/image%20(1).png)

Já para o terceiro exemplo de teste, tem-se:

![](https://raw.githubusercontent.com/lucasbbs/APC-2020.2/main/itera%C3%A7%C3%A3o/questao6/image%20(3).png)

* For example:

|Input|Result|
|-----|------|
|10<br>0<br>2<br>5<br>0<br>1<br>1<br>0<br>0<br>2<br>2<br>0<br>-1|7|
|2<br>0<br>1<br>2<br>1<br>2<br>-1|Lar Deivis lar|
|5<br>0<br>1<br>5<br>0<br>2<br>3<br>2<br>2<br>1<br>5<br>-1|4|
|2<br>0<br>0<br>-1|Lar Deivis lar|
|87995<br>0<br>2<br>16679<br>1<br>61504<br>0<br>2<br>40712<br>1<br>66741<br>2<br>44761<br>0<br>2<br>9291<br>1<br>25898<br>0<br>0<br>2<br>35733<br>1<br>84824<br>1<br>25419<br>0<br>1<br>81046<br>1<br>76895<br>2<br>81225<br>0<br>1<br>59424<br>2<br>71417<br>2<br>83579<br>0<br>0<br>0<br>0<br>1<br>48738<br>0<br>0<br>0<br>0<br>1<br>65052<br>2<br>73585<br>1<br>36387<br>2<br>26971<br>0<br>1<br>23532<br>0<br>0<br>2<br>72664<br>1<br>43919<br>1<br>41588<br>1<br>4187<br>1<br>23983<br>0<br>2<br>38541<br>1<br>68851<br>2<br>7541<br>1<br>82847<br>0<br>1<br>81702<br>2<br>53440<br>0<br>0<br>0<br>1<br>3921<br>0<br>1<br>42085<br>2<br>55755<br>2<br>43539<br>2<br>60457<br>1<br>60263<br>1<br>65501<br>2<br>46751<br>2<br>44531<br>2<br>79311<br>2<br>56956<br>2<br>65569<br>1<br>11008<br>1<br>78907<br>0<br>2<br>41097<br>0<br>-1<br>|21|
|74516<br>0<br>0<br>1<br>65411<br>2<br>74510<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>-1|10|
