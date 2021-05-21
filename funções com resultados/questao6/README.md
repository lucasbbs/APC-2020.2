# Uma vida musical
Gustavo e Nathan são estudantes de Ciência da Computação na UnB, mas o último semestre que eles fizeram foi muito puxado e eles estão muito cansados. Eles decidiram então, como grandes amigos, tomar um ano sabático e rodar pelo Brasil tentando fazer o que eles gostam, música. Como são estudantes, não terão muito recursos, então sempre irão trocar seus instrumentos com outros artistas para ter novas experiências e aprender novos instrumentos. Mas isso trouxe um problema, pois as vezes o novo instrumento pode não caber no carro deles. Você irá então ajudá-los! Crie um função areaInstrumento que irá receber três argumentos: dois inteiros **_n_**,**_m_** correspondendo ao instrumento de forma retangular usado por Nathan e um inteiro **_r_** correspondendo ao lado do triângulo equilátero que equivale ao instrumento que Gustavo toca. Calcule a área de ambos os instrumentos e retorne a soma deles.

* Entrada

A entrada consiste nos parâmetros da função **areaInstrumento**, que são os três números inteiros **_n_**, **_m_** e **_r_** **(2 ≤ _n_, _m_, _r_ ≤ 100)** como descritos no enunciado.

* Saída

Sua função deve retornar a soma da área de ambos os instrumentos.

* Observações

No primeiro caso de teste, o resultado é \(28.89711\) pois a área do instrumento de Nathan é 25 e a área do instrumento do Gustavo é **3.89711**. Use o método sqrt(**_x_**)  da biblioteca math para auxiliar no cálculo da área do triângulo.
Não se preocupe com arredondamentos, o próprio juiz fará o truncamento para **5** casas decimais.
Submeta somente o que foi solicitado no enunciado da questão.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print("{0:.5f}".format(areaInstrumento(5,5,3)))|28.89711
print("{0:.5f}".format(areaInstrumento(5,6,8)))|57.71281
print("{0:.5f}".format(areaInstrumento(7,20,100)))|4470.12702
print("{0:.5f}".format(areaInstrumento(15,35,43)))|1325.64049
print("{0:.5f}".format(areaInstrumento(18,3,23)))|283.06372
print("{0:.5f}".format(areaInstrumento(73,4,30)))|681.71143
