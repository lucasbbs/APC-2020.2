# A Origem
Em "A Origem", o diretor Jeremias Nolan estava interessado em mostrar que seus sonhos podem ser hackeados. Para isso, ele implementou uma função chamada sonho que tem como parâmetro um número inteiro e, quando chamada recursivamente, é capaz de criar sonhos dentro de sonhos. Essa função também lê um número inteiro (input), e quando esse valor é par significa que Jeremias deve voltar a realidade, mas quando esse número é ímpar, Jeremias deve ir mais fundo no seu subconsciente começando um novo sonho. Para manter um "rastro" e não se perder nas diversas camadas de sonho, Jereminas utiliza o parâmetro de entrada do sonho como contador e este é incrementado em 1 e impresso, toda vez que ele "entra" em um novo sonho.

Sua tarefa é implementar a função do Jeremias para poder vivenciar a sua experiência.

* Entrada
A função sonho tem como único parâmetro um número inteiro não-negativo n, para ser utilizado como contador. Além disso, a função deve ler um outro número inteiro x da entrada padrão, obedecendo a formatação de input dos testes apresentados.

* Saída
A saída do programa deve ser o valor do contador nos diversos níveis de sonho, de acordo com os exemplos.

* Observações
No primeiro caso de teste, o contador começa em zero e seu valor é impresso apenas na primeira chamada da função sonho.
No segundo caso de teste, o contador começa em **1** e com a leitura dos inteiros, na ordem **3**,**3**,**3** e **2**, Jeremias entra em outros **3** sonhos, resultando na impressão dos inteiros **2**, **3**, **4** e **5**. Observe que Jeremias interrompe seus sonhos após o inteiro **2** ser lido.
No terceiro caso de teste, o contador começa em **2** e com a leitura dos inteiros, na ordem **1**, **1**, **1** e **2**, outros **3** sonhos ocorrem, resultando na impressão dos inteiros **3**, **4**, **5** e **6**. Os sonhos de Jeremias são interrompidos após o inteiro **2** ser lido.
Submeta somente o que foi solicitado.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).



* For example:

Test|Input|Expected
----|-----|--------
sonho(0)|2|1
sonho(1)|3<br>3<br>3<br>2|2<br>3<br>4<br>5
sonho(2)|1<br>1<br>1<br>2|3<br>4<br>5<br>6
sonho(3)|1<br>3<br>5<br>7<br>9<br>11<br>13<br>15<br>17<br>19<br>21<br>21<br>19<br>17<br>15<br>13<br>11<br>9<br>7<br>5<br>3<br>1<br>2|4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26
sonho(3)|1<br>2|4<br>5
sonho(4)|2|5
