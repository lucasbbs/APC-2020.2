# Comprimento de Papel

| column 1 | column 2 |
|:----------:|----------|
| value | value 1<br>value 2 |
| value | value 1<br>value 2 |

No ano passado, Dr. Mike, um profissional renomado na área de Design, está planejando revolucionar a indústria de produção de papel com uma nova invenção de tamanhos de papel! O problema é que Dr. Mike sofre da síndrome do impostor e não conseguiu definir a largura do seu novo formato de papel.

Esse é o seu momento de brilhar! Ajude o Dr. Mike com sugestões de comprimento de papel, criando um Programa para imprimir como o papel ficaria caso tivesse a opção de comprimento escolhida por você, junto da largura escolhida pelo Dr. Mike.  Para isso você deve implementar uma função chamada print_rectangle que recebe esse valor e imprime o papel.

Ah! Você tem fixação pelo número 4! Esta é sempre sua opção de comprimento.

* Entrada 
A entrada consiste de 3 inteiros guardados pelas variáveis a,b,c≥4, separadas por espaço.

* Saída
Para cada um dos 3 tamanhos escolhidos pelo Dr. Mike, você deve imprimir como ficaria a piscina usando o seguinte formato:

O comprimento do papel
As bordas do papel usando o caractere (x).
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, caso a criação não tenha sido feita corretamente (sendo case-sensitiveo nome da função).

For example:

|Input|Expected
|-----|--------
|4 5 6 |4<br>xxxx<br>x&nbsp;&nbsp;x<br>x&nbsp;&nbsp;x<br>xxxx<br>5<br>xxxxx<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>xxxxx<br>6<br>xxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxx
|6 7 8 |6<br>xxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxx<br>7<br>xxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxx<br>8<br>xxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxx 
|9 10 11 |9<br>xxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxx<br>10<br>xxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxx<br>11<br>xxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxx 
|5 5 5 |5<br>xxxxx<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>xxxxx<br>5<br>xxxxx<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>xxxxx<br>5<br>xxxxx<br>x&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;x<br>xxxxx 
|12 16 20 |12 <br> xxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxx<br><br>16<br>xxxxxxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxxxxxx<br>20<br>xxxxxxxxxxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxxxxxxxxxx
|24 30 45 |24<br>xxxxxxxxxxxxxxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxxxxxxxxxxxxxx<br>30<br>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>45<br>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
