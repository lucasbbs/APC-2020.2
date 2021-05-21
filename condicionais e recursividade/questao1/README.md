# Área de Figuras Planas II
Implemente uma função chamada area que imprime a área de uma determina figura geométrica. A função deve receber 3 parâmetros, sendo dois deles valores numéricos e uma string representando a forma geométrica. A área da figura deve ser do tipo inteiro. As formas geométricas permitidas são "retangulo", "losango" e "triangulo".

* Entrada
Os parâmetros da função são dois inteiros _arg_1, _arg_2 ≥ 1 e uma string forma. Em caso de retângulo ou triângulo, os argumentos representam a base e a altura da forma e caso a figura seja um losango, os argumentos representam o valor das duas diagonais.

* Saída
A função deve imprimir a frase "O forma tem area de area".

_**forma**_ é a string inserida, que pode tomar o nome de quatro formas geométricas: **retangulo**, **losango** e **triangulo** e _area_ é somente o valor **inteiro** do cálculo da área da forma geométrica dada na string **_forma_**, com arg1,arg2 assumindo as incógnitas de cada cálculo de área.

* Observações
Submeta somente o que foi solicitado.

* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).



* For example:

|Input|Expected
|-----|--------
|area(10, 2, 'losango')|O losango tem 10 de area
|area(20, 4, 'retangulo')|O retangulo tem 80 de area
|area(15, 3, 'triangulo')|O triangulo tem 22 de area
|area(144, 198, 'losango')|O losango tem 14256 de area
|area(72, 30, 'triangulo')|O triangulo tem 1080 de area
|area(194, 193, 'retangulo')|O retangulo tem 37442 de area
