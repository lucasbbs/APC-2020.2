# Números Maravilhosos
Números Maravilhosos constituem um problema muito bem conhecido no meio da matemática. Esse problema tem diversos outros nomes e um deles é a Conjectura de Siracusa. Uma conjectura em matemática é uma proposição ou sentença tida como verdade que, no entanto, nunca foi provada. Quando é provada ser verdadeira ela passa a ser um Teorema. A Conjectura de Siracusa tem o seguinte enunciado: **"A partir de qualquer número n, dividindo-o por 2 se for par, ou multiplicando por 3 e adicionando 1 se for ímpar, e fazendo assim sucessivamente, chegaremos sempre ao número 1".**

De uma maneira recursiva, esse problema pode ser visto da seguinte forma:

![equation](http://www.sciweavers.org/tex2img.php?eq=maravilhosos%28x%29%20%3D%5Cbegin%7Bcases%7D1%20%26%20se%20%5C%3A%20%20x%20%3D%201%5C%5Cmaravilhosos%283x%2B1%29%20%26%20se%20%5C%3A%20x%5C%3A%20for%5C%3A%20impar%5C%5Cmaravilhosos%20%5Cbig%28%20%5Cfrac%7Bx%7D%7B2%7D%5Cbig%29%20%26%20se%20%5C%3A%20x%5C%3A%20for%5C%3A%20par%5Cend%7Bcases%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Dessa forma, implemente um programa para receber um valor **_x_** e imprimir a sequência de números que **_x_** irá tomar até que seu valor alcance **1**. Seu programa deve possuir uma função recursiva chamada maravilhosos com um parâmetro chamado **x** que irá receber um valor e deverá imprimir recursivamente a aplicação da função até que o caso base (valor 1) seja alcançado.

* Entrada
A entrada consiste de 1 inteiro x tal que (**1< _x_ <10⁵**). Não é necessário validar se os números estão dentro do intervalo definido.

* Saída
Cada linha da saída deve possuir um inteiro da sequência até o número um, conforme os exemplos.

* Observações
No primeiro caso de teste, o contador começa em 4 e seu valor é impresso na primeira chamada a função. Sendo 4 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 2 que é impresso na tela. Sendo 2 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 1 que é impresso na tela. No caso do número 1 a função encerra sua execução.
No segundo caso de teste, o contador começa em 5 e seu valor é impresso na primeira chamada a função. Sendo 5 um número ímpar, a função maravilhosos foi chamada novamente passando como parâmetro o número 16 que é impresso na tela. Sendo 16 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 8 que é impresso na tela. Sendo 8 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 4 que é impresso na tela. E assim a execução segue o mesmo caminho descrito no primeiro caso de teste.
No terceiro caso de teste, o contador começa em 7 e seu valor é impresso na primeira chamada a função. Sendo 7 um número ímpar, a função maravilhosos foi chamada novamente passando como parâmetro o número 22 que é impresso na tela. Sendo 22 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 11 que é impresso na tela. Sendo 11 um número ímpar, a função maravilhosos foi chamada novamente passando como parâmetro o número 34 que é impresso na tela. Bem, acho que você entendeu não é?  
Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:
