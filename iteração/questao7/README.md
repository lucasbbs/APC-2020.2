# Triângulo Descrescente
Utilizando laços aninhados, receber um inteiro n do usuário e imprimir a seguinte estrutura (sem o parêntesis):

Se **_n_** for par:

**( _n_ ) ( _n_ − 2 ) ( _n_ − 4 ) … ( 0 )**

**( _n_ − 2 ) ( _n_ − 4 ) … ( 0 )**

**( _n_ − 4 ) … ( 0 )**

**…**

**( 0 )**

Se **_n_** for ímpar:

**( _n_ ) ( _n_ − 2 ) ( _n_ − 4 ) … ( 1 )**

**( _n_ − 2 ) ( _n_ − 4 ) … ( 1 )**

**( _n_ − 4 ) … ( 1 )**

**…**

**( 1 )**

* Entrada

A entrada consiste de um inteiro 0<n≤100.

* Saída

A saída deve conter o padrão conforme o apresentado e os exemplos a seguir, onde os números em uma linha estão todos separados por um espaço.

* For example:

|Input|Result|
|-----|------|
|5|5 3 1<br>3 1<br>1|
|6|6 4 2 0<br>4 2 02 0<br>0|
|10|10 8 6 4 2 0<br>8 6 4 2 0<br>6 4 2 0<br>4 2 0<br>2 0<br>0|
|25|25 23 21 19 17 15 13 11 9 7 5 3 1<br>23 21 19 17 15 13 11 9 7 5 3 1<br>21 19 17 15 13 11 9 7 5 3 1<br>19 17 15 13 11 9 7 5 3 1<br>17 15 13 11 9 7 5 3 1<br>15 13 11 9 7 5 3 1<br>13 11 9 7 5 3 1<br>11 9 7 5 3 1<br>9 7 5 3 1<br>7 5 3 1<br>5 3 1<br>3 1<br>1|
|42|42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>28 26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>26 24 22 20 18 16 14 12 10 8 6 4 2 0<br>24 22 20 18 16 14 12 10 8 6 4 2 0<br>22 20 18 16 14 12 10 8 6 4 2 0<br>20 18 16 14 12 10 8 6 4 2 0<br>18 16 14 12 10 8 6 4 2 0<br>16 14 12 10 8 6 4 2 0<br>14 12 10 8 6 4 2 0<br>12 10 8 6 4 2 0<br>10 8 6 4 2 0<br>8 6 4 2 0<br>6 4 2 0<br>4 2 0<br>2 0<br>0|
|1|1|
