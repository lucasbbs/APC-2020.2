# Prefix Sum
Um conceito muito utilizado na Computação é o de soma de prefixos ou prefix sum. O prefix sum é um vetor que possui a soma cumulativa dos valores de um outro vetor, da seguinte forma: dada uma sequência de números **_x_ ₁, _x_ ₂, _x_ ₃, …, _x_ ₙ**, pode-se obter uma segunda sequência de números **_y_ ₁, _y_ ₂, _y_ ₃, …, _y_ ₙ**, conhecida como somas de prefixos, que são dadas pelo seguinte:

**_y_ ₁= _x_ ₁**

**_y_ ₂= _x_ ₁+ _x_ ₂**

**_y_ ₃ = _x_₁ + _x_₂ + _x_₃**

**…**

Assim, crie um algoritmo que receba um vetor de inteiros e retorne o vetor da soma de prefixos desse vetor.

* Entrada
A primeira linha contém **_N_ (1 ≤ _N_ ≤ 50)** números inteiros **_x_ ₁, _x_ ₂, ..., _x_ ₙ** separados por espaço em branco, em que **_xᵢ_ (0 ≤ _xᵢ_ ≤ 10000)** representa o valor da **_i_**-ésima posição desse vetor de inteiros.

* Saída
Imprima na primeira linha o vetor com as somas de prefixos e na segunda linha o vetor de inteiros lido da entrada. Todos os valores dos vetores devem ser impressos separados por espaço.

* Observações
No primeiro exemplo de teste, o vetor de somas prefixas **_y_ ₁ = _x_ ₁ = 1**, **_y_ ₂ = _x_ ₁ + _x_ ₂ = 1 + 2 = 3** e **_y_ ₃ = _x_ ₁ + _x_ ₂ + _x_ ₃ = 1 + 2 + 3 = 6**.

* For example:

Input|Result
-|-
1 2 3|1 3 6<br>1 2 3
26 24 67|26 50 117<br>26 24 67
60 93 4 34 44 47 15 51|60 153 157 191 235 282 297 348<br>60 93 4 34 44 47 15 51
58 61 62 49 85 82 59 23 10 30 9 17 90|58 119 181 230 315 397 456 479 489 519 528 545 635<br>58 61 62 49 85 82 59 23 10 30 9 17 90
30 73 68 22 94 58 17 64 1 18 57 33 49 61 87 23 25 91|30 103 171 193 287 345 362 426 427 445 502 535 584 645 732 755 780 871<br>30 73 68 22 94 58 17 64 1 18 57 33 49 61 87 23 25 91
17 21 95 98 37 86 64 11 50 79 0 47 66 23 32 64 96 76 81 7 66 16 25|17 38 133 231 268 354 418 429 479 558 558 605 671 694 726 790 886 962 1043 1050 1116 1132 1157<br>17 21 95 98 37 86 64 11 50 79 0 47 66 23 32 64 96 76 81 7 66 16 25
