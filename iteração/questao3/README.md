# Tribo
Gabigué está cansado dessa vida tecnológica, não aguentando mais ver fórmulas matemáticas. Por isso, ele decidiu viver em uma tribo. Foi aí que ele ficou sabendo que, até para entrar na tribo ancestral, ele deveria saber algumas fórmulas básicas e determinar a soma dos termos de uma sequência de números inteiros. Sabe-se que tal sequência é composta por **_n_** inteiros **_s₁_**,**_s₂_**,…,**_sₙ_**, em que o **_i_**-ésimo termo si dessa sequência, para **_i_** **= 1,2,3,…,** **_n_**, é definido conforme a validação da primeira propriedade dentre as quatro estabelecidas a seguir, considerando a ordem de prioridade:

1. Se **_i_** é um número primo, si é igual o quadrado dele;
2. Se **_i_** for uma potência de dois, si assume o valor do índice do MSB (Most Significant Bit) da representação binária de **_i_**;
3. Se **_i_** for um número par, si é igual a **_i_** dividido por **2**;
4. Se nenhuma das propriedades forem validadas, **_sᵢ=i_**. 

Como Gabigué odeia matemática, ele contratou você para resolver esse problema para que ele finalmente possa viver em paz. Sua tarefa consiste em determinar a soma **_S_** de todos os seus termos da sequência **_s₁_**,**_s₂_**,…,**_sₙ_**, ou seja, **_S = s₁ + s₂ + … + sₙ_**. 

* Entrada

A entrada consiste em um inteiro **_n_** (**1 ≤ _n_ ≤ 10000**), relacionado à quantidade de termos da sequência.



* Saída

Seu programa deve imprimir um número inteiro, a soma **_S = s₁ + s₂ + … + sₙ_**.

* Observações

No primeiro caso de teste, o resultado é **40** pois **_S_ = 0 + 4 + 9 + 2 + 25**.

* For example:

|Input|Result|
|-----|------|
|5|40|
|1|0|
|10|109|
|8|95|
|25|1698|
|31|3569|
