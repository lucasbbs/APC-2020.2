# MDC
O máximo divisor comum (MDC) entre dois ou mais números inteiros é o maior número inteiro que é fator de todos eles. Por exemplo, os divisores comuns de 12 e 18 são 1, 2, 3 e 6, logo o **_mdc_(12,18) = 6**. No ano 300 a.c., o livro Elementos descreve um método para encontrar o MDC de dois números que é utilizado até os dias atuais, e é conhecido como Algoritmo de Euclides. Esse método baseia-se na seguinte propriedade: **_mdc_(_a_,_b_)==_mdc_(_b_,_r_)**, onde **_r_** é o resto da divisão de **_a_** por **_b_**. Dessa forma, aproveitando-se dessa propriedade, é possível realizar sucessivas divisões entre pares de valores e seus restos, até que o resto de alguma divisão seja zero. Quando o resto passa a ser zero, o segundo elemento do último mdc realizado é o MDC dos pares iniciais. O algoritmo funciona da seguinte maneira:

**_mdc_(32,26)** - o resto da divisão de 32 por 26 é 6

**_mdc_(26,6)** - o resto da divisão de 26 por 6 é 2

**_mdc_(6,2)** - o resto da divisão de 6 por 2 é 0

**_mdc_(2,0)** - o resultado é 2, para mdc(32,26)

Dessa forma, é possível escrever um algoritmo recursivo para o método de euclides da seguinte forma:

![equation](http://www.sciweavers.org/tex2img.php?eq=mdc%28a%2C%20b%29%20%3D%20%5Cbegin%7Bcases%7D%20a%20%26%20%5Ctext%7Bse%20%7D%20b%20%3D%200%20%5C%5C%20mdc%28b%2C%20a%20%5C%25%20b%29%20%26%20%5Ctext%7Bse%20%7D%20a%20%5C%25%20b%20%3E%200%2Cb%20%3E%200%20%5Cend%7Bcases%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)



Dada a especificação recursiva para o algoritmo de euclides, sua tarefa é implementar uma função **mdc(a, b)** que calcule o MDC entre dois números a e b.

* Entrada
A entrada consiste de dois inteiros a e b que representam os valores cujo MDC é procurado ( 1 ≥ a,b ≥ 10¹⁵).

* Saída
A função deve retornar o MDC entre os valores **_a_** e **_b_**, conforme o exemplo.

* Observações
Submeta somente o que foi solicitado.

No primeiro exemplo de teste, o MDC entre 6 e 6 é calculado conforme a propriedade mencionada: mdc(6,6)=mdc(6,0), resultando em 6.

No segundo exemplo de teste, o MDC entre 12 e 30 é calculado conforme a propriedade mencionada: mdc(12,30)=mdc(30,12)=mdc(12,6)=mdc(6,0), resultando em 6.

No terceiro exemplo de teste, o MDC entre 105 e 60 é calculado conforme a propriedade mencionada: mdc(105,60)=mdc(60,45)=mdc(45,15)=mdc(15,0), resultando em 15.

* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

Input|Expected
-----|--------
print(mdc(6,6))|6
print(mdc(12,30))|6
print(mdc(105,60))|15
print(mdc(139,10))|1
print(mdc(105,460))|5
print(mdc(1546986256,41))|1
