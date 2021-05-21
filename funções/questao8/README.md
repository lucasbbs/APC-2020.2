# Piscina da Mansão
No ano passado, Prof. Nerynho havia publicado sua pesquisa na conferência mais aclamada do mundo ocidental, All Papers Considered (APC), e como prêmio pela maior contribuição ao mundo acadêmico, ganhou uma mansão no Lago Sul.  Ele está meio entediado na pandemia e quer construir uma piscina para ficar deitado e tomar suco de laranja enquanto lê bons livros de teoria da Ciência da Computação. 

Seu número preferido é 3 e por isso ele gosta sempre de ter 3 opções disponíveis. Dessa forma, sua tarefa é criar um Programa para imprimir como a piscina ficaria com cada uma das três opções de comprimento. Para isso você deve implementar uma função chamada print_rectangle que recebe esse valor e imprime a piscina.

* Entrada:
A entrada consiste de 3 números diferentes guardados pelas variáveis ![equation](http://www.sciweavers.org/tex2img.php?eq=a%2Cb%2Cc%20%5Cgeq%20%203&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0), separadas por espaço.

* Saída:
Para cada um dos 3 tamanhos, você deve imprimir como ficaria a piscina usando o seguinte formato:

O comprimento da piscina
As bordas da piscina usando o caractere (+).
Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

|Input|Expected
|-----|--------
|3 4 5 |3
||+++
||+&nbsp;+
||+++
||4
||++++
||<pre>+  +</pre>
||++++
||5
||+++++
||<pre>+   +</pre>
||+++++ 
||

|Input|Expected
|-----|--------
|6 7 8 |6
||++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++
||7
||+++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||+++++++
||8
||++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++ 
||

|Input|Expected
|-----|--------
|9 10 11 |9
||+++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||+++++++++
||10
||++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++++
||11
||+++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||+++++++++++ 
||

|Input|Expected
|-----|--------
|5 5 5|5
||+++++
||+&nbsp;&nbsp;&nbsp;+
||+++++
||5
||+++++
||+&nbsp;&nbsp;&nbsp;+
||+++++
||5
||+++++
||+&nbsp;&nbsp;&nbsp;+
||+++++ 
||

|Input|Expected
|-----|--------
|12 16 20 |12
||++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++++++
||16
||++++++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++++++++++
||20
||++++++++++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 
||++++++++++++++++++++

|Input|Expected
|-----|--------
|24 30 45 |24
||++++++++++++++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++++++++++++++++++
||30
||++++++++++++++++++++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||++++++++++++++++++++++++++++++
||45
||+++++++++++++++++++++++++++++++++++++++++++++
||+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+
||+++++++++++++++++++++++++++++++++++++++++++++ 

<pre>
