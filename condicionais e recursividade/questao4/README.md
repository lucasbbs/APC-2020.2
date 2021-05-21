# Área de Figuras Planas III
Implemente uma função chamada area que imprime a área de uma determina figura geométrica. A função deve receber 3 parâmetros, sendo dois deles valores numéricos e uma string representando a forma geométrica. A área da figura deve ser do tipo inteiro. As formas geométricas permitidas são retangulo, losango, triangulo e circulo. 

* Entrada
Os parâmetros da função são dois inteiros _arg_1, _arg2_ ≥ 1 e uma string _forma_. Em caso de retângulo ou triângulo, os argumentos representam a base e a altura da forma, caso a figura seja um losango, os argumentos representam o valor das duas diagonais, e caso a figura geométrica seja círculo, a variável **_arg1_** será **sempre** o raio, e a variável **_arg2_** **sempre** será igual a 3.

* Saída
A função deve imprimir a frase O **_forma_** tem _**area**_ de area

Onde **_forma_** é a string inserida, que pode tomar o nome de quatro formas geométricas: **retangulo**, **losango**, **triangulo**, **circulo** e **_area_** é somente o valor **inteiro** do cálculo da área da forma geométrica dada na string **_forma_**, com **_arg1_**, **_arg2_** assumindo as incógnitas de cada cálculo de área.

* Observação
Caso a figura seja um círculo, utilize **_arg2_** no lugar do valor de **π**, para calcular a área.
Submeta somente o que foi solicitado.
Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

Input|Expected
-----|--------
area(10, 2, 'losango')|O losango tem 10 de area
area(20, 4, 'retangulo')|O retangulo tem 80 de area
area(15, 3, 'circulo')|O circulo tem 675 de area
area(144, 198, 'losango')|O losango tem 14256 de area
area(72, 30, 'triangulo')|O triangulo tem 1080 de area
area(194, 193, 'retangulo')|O retangulo tem 37442 de area
