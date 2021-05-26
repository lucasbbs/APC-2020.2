# Bob e seus datagramas
Alice e Bob são personagens lendários usados para apresentar de maneira didática situações onde há uma comunicação entre duas entidades A e B.

Imagine que Bob deseja enviar uma imagem para Alice. Na Internet, isto é feito quebrando a imagem em vários pedaços, chamados de datagramas, e enviando um datagrama de cada vez. O problema é que os datagramas podem se espalhar por diferentes caminhos para chegarem ao seu destino. Deste modo, os datagramas podem chegar desordenados ao computador de Alice. Para evitar esta confusão, os datagramas são enviados por Bob com um número de sequência. Bob sempre envia um datagrama com um número de sequência maior que o número de sequência do datagrama que foi enviado por último.

Desta maneira, Alice pode reconstruir a imagem simplesmente ordenando os datagramas que ela recebeu, pelos respectivos números de sequência. Mas antes de fazer isto, Alice te pediu ajuda para calcular um número.

Ela quer saber quantas inversões aconteceram no envio da imagem. O número de inversões é o número de pares **{Sᵢ,Sⱼ}** tais que **_i_ < _j_** e **Sᵢ > Sⱼ** onde **S₁** é o número de sequência do datagrama que chegou primeiro, **S₂** é o número de sequência do datagrama que chegou em segundo lugar, S₃ é o número de sequência do datagrama que chegou em terceiro lugar, e assim por diante.

* Entrada
A primeira e única linha contém uma sequência de **_N_ (1 ≤ _N_ ≤ 10³)** inteiros não-negativos **Sᵢ(1 ≤ Sᵢ ≤ 10⁹)** que são os números de sequência dos datagramas em ordem de chegada ao computador de Alice.

* Saída
Imprima uma linha com o número de inversões, como descrito no enunciado (o número de pares tais que **_i_ < _j_** e **Sᵢ > Sⱼ** ).

* Observações
No segundo caso teste, o número 5 gera situações de inversão com os números **2**, **3**, e **4**. Portanto o número de inversões é **3**.
  
No terceiro caso de teste, o número 5 gera situações de inversão com os números  **2**, **4** e **3** e o número **4** gera inversão com o número **4**.  Portanto o número de inversões é **4**.
  
* For example:


|Input|Result|
|-----|------|
|1 4 5 9 15|0|
|1 5 2 3 4|3|
|1 5 2 4 3|4|
|5 4 3 2 1|10|
|2239 306784401 9149179 0 884939 1000000000 740 54038 9983 1 63888 9698 2 67963 78 37207 921339 948359 55 279528 4 341002 823 21 1299 185735498 824948933 93255364 22 607066 834148 75193839 994184|230|
|6940 84092800 762 3837 217 69998638 38821 886 5 555693504 977 993807865 9579134 7 78 952311 56 1000000000 781793032 1237847 769272 55355425 4405 9234062 6714 36 41 56769414 916 897001113 0 919408 1773|272|
