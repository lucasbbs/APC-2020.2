# Estatísticas II
Dado um conjunto de números de inteiros X={x₁,x₂,…,xₙ}, podemos calcular seu desvio padrão (σ) como:

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Csigma%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Csum%5Climits_%7Bi%3D1%7D%5E%7BN%7D%20%28x_i%20-%20%5Cbar%7Bx%7D%29%5E2%7D%7BN%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

em que **_x̄_** representa a média dos valores de **_X_**.

Dessa forma, escreva um programa que calcule a média e a variância de **_X_**

* Entrada

A entrada consiste de N ( 1≤N≤100 ) números inteiros x1,x2,…,xN (−103≤xi≤103,i=1,…,N) separados por espaço em branco.

* Saída

Imprima duas linhas, em que cada uma contém um valor em ponto flutuante com uma casa decimal de precisão. A primeira linha deve apresentar a média de X, enquanto que a segunda linha deve apresentar o desvio padrão de X.

* Observações

No primeiro caso de teste, a média dos valores da lista é ( 16 + 24 + 30)/3 = 20.0. O desvio padrão é calculado por ![equation](http://www.sciweavers.org/tex2img.php?eq=%5Csqrt%7B%2816%20-20%29%5E2%20%2B%20%2824-20%29%5E2%2B%2820-20%29%5E2%29%2F3%20%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

* For example:

|Input|Result|
-|-
|16 24 20|20.0<br>3.3|
|-85 77 44 -12|6.0<br>61.4|
|-12 -87 -86 -90 -34 -94 -97 -36 79|-50.8<br>54.7|
|-43 6 59 -89 34 -88 30 20 -57 -16|-14.4<br>49.9|
|-37 -25 -49 -17 -42 -46 96 -36 93 71 81 49 -50 -5 69|10.1<br>56.3|
|-59 -29 -28 -79 64 76 38 83 76 100 -37 -11 -68 -64|4.4<br>62.8|
