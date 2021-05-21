# O Gato e a Bolinha
Johnin está entediado em casa durante a quarentena, e para fazer algo decidiu brincar com seu gato, Batatinha. Johnin quer ensinar seu gato a buscar uma bolinha. Seria melhor brincar disso com um cachorro, porque gatos são muito preguiçosos, mas "quem não tem cão, brinca com o gato".

Batatinha, um gato preguiçoso e um pouco acima do peso, sempre toma o **menor** caminho até a bolinha. Sendo um gato ele passa por cima ou por baixo de qualquer móvel que esteja entre ele e a bolinha,  então você pode assumir que não existem obstáculos no caminho.

Além disso, Batatinha só vai atrás da bolinha se a distância entre ele e a bola for menor ou igual que **_k_** metros. Se a bolinha estiver a **menos** de **_k_** metros de distância, Batatinha diz ***miau* ta bom, vou buscar** e vai buscar a bolinha. Se ela estiver a **exatamente** **_k_** metros, ele diz **pfff... ta bom**. Se estiver a **mais** do que **_k_** metros, ele diz **ta achando que eu sou cachorro?** e olha de cara feia para Johnin.

Sua tarefa é escrever um programa que, dada a posição de Batatinha e a posição onde a bola foi arremessada, diga qual a reação do gato.

Para isso, você deve usar a função sqrt da biblioteca math do Python. Para importar e usar essa função veja o exemplo abaixo.

import math
x = math.sqrt(4) # x recebe 2
* Dica: Python possui o operador de exponenciação ** (e.g. x = 2**2)

* Entrada

A entrada possui 5 linhas. Em cada linha você tem um número inteiro.
A primeira linha é o número k (0<k≤200), a distância máxima que Batatinha vai andar atrás da bolinha.
As próximas quatro linhas são quatro números inteiros, x1, y1, x2, y2, respectivamente. x1, y1 são as coordenadas do gato. x2, y2 são as coordenadas da bolinha.
* Saída

Sua função deve imprimir a reação de Batatinha ao arremesso, conforme descrito:

Se a bolinha estiver a menos de k metros de distância, imprima *miau* ta bom, vou buscar
Se a bolinha estiver a exatamente k metros de distância, imprima pfff... ta bom
Se a bolinha estiver a mais de k metros de distância, imprima ta achando que eu sou cachorro?
* Observações

No primeiro caso de teste, a distância entre Batatinha e a bolinha é 3, e a distância máxima (k) é 4, então o resultado é *miau* ta bom, vou buscar.
No segundo caso de teste, a distância entre Batatinha e a bolinha é exatamente 4, e k também é 4, logo o resultado é pfff... ta bom.
No terceiro caso de teste, a distância entre Batatinha e a bolinha é 5, e k é 4. Então o resultado é ta achando que eu sou cachorro?

* For example:

Input|Expected
-----|--------
4<br>1<br>1<br>1<br>4|*miau* ta bom, vou buscar
4<br>1<br>1<br>1<br>5|pfff... ta bom
4<br>1<br>1<br>1<br>6|ta achando que eu sou cachorro?
10<br>0<br>0<br>5<br>0|*miau* ta bom, vou buscar
10<br>0<br>0<br>5<br>5|*miau* ta bom, vou buscar
10<br>0<br>0<br>7<br>8|ta achando que eu sou cachorro?
