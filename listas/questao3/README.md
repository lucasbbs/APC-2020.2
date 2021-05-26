# Correndo na pista I
Palmério está treinando para uma meia maratona e todos os domingos realiza seus treinos em uma pista de atletismo, que possui formato oval e comprimento de 400 metros. Nesse treino, ele percorre **_N_** voltas na pista e registra o tempo gasto (em segundos) para percorrer cada uma dessas voltas.

Ao retornar para casa, Palmério estuda seu desempenho no treino da seguinte maneira: ele identifica o menor tempo **_tₘᵢₙ_** registrado ao completar uma volta. Em seguida, ele analisa, volta a volta, o tempo que seria necessário descontar em cada volta para percorrer todas as voltas no tempo **_tₘᵢₙ._**

Como Palmério pode ter percorrido várias voltas nessa pista, pode ser difícil fazer essas contas manualmente e, por isso, ele pede sua ajuda. Escreva um programa que calcule a diferença de tempo entre cada volta e o tempo **_tₘᵢₙ._**

* Entrada

A primeira linha da entrada contém um número inteiro **_N_ (1 ≤ _N_ ≤ 100)** indicando a quantidade de voltas percorridas na pista por Palmério em um treino. A segunda linha da entrada contém **_N_** inteiros separados por espaço em branco **_a_ ₁, _a_ ₂, …, _a_ ₙ**, em que **_aᵢ_ (1 ≤ aᵢ ≤ 300)** indica o tempo (em segundos) percorrido por Palmério na **_i_**-ésima volta.

* Saída

Imprima **_N_** números inteiros separados por espaço em branco **_b_ ₁, _b_ ₂, …, _b ₙ_,** em que **_bᵢ_** é a diferença de tempo entre a volta **_i_** e **_tₘᵢₙ_**, e que **_bᵢ_ ≥ 0**.

* Observações

No primeiro caso de teste o menor tempo é 15, então o tempo que deve descontado de cada tempo que Palmério informou é 20-15 = 5, 15 - 15 = 0, 23 - 15 = 8, 17 - 15 = 2 e 16 - 15 = 1

* For example:

|Input|Result|
|-|-|
|5<br>20 15 23 17 16|5 0 8 2 1|
|4<br>13 19 18 13|0 6 5 0|
|6<br>50 51 51 50 30 35|20 21 21 20 0 5|
|22<br>174 197 180 147 189 199 115 114 127 150 178 179 119 103 176 166 150 185 199 107 174 145|71 94 77 44 86 96 12 11 24 47 75 76 16 0 73 63 47 82 96 4 71 42|
|5<br>10 50 55 65 75|0 40 45 55 65|
|10<br>73 56 87 16 43 29 64 73 99 45|57 40 71 0 27 13 48 57 83 29|
