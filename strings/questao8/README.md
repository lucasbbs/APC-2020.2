# Genoma
Semana passada a tumba do lendário feiticeiro Mellin foi aberta para que cientistas ao redor do mundo decodificassem seu DNA.

Essa tarefa está quase acabando, só o que falta é recuperar alguns nucleotídeos de uma cadeia s. Cada nucleotídeo é codificado como uma letra maiúscula do alfabeto português: "A", "C", "G" ou "T". Nucleotídeos não reconhecidos são codificados com um ponto de interrogação "?". Assim, s é uma cadeia com caracteres "A", "C", "G", "T" e "?".

Sabe-se que em uma cadeia, cada nucleotídeo deve aparecer um número igual de vezes.

Sua tarefa é decodificar o genoma e substituir cada nucleotídeo não-reconhecido por um dos quatro tipos reconhecidos de modo que o número de cada um dos quatro tipos seja igual.



* Entrada
A primeira linha contém um inteiro **_n_ (4 ≤ _n_ ≤ 255)**, representando o comprimento do genoma.

A segunda linha contém a string **_s_** de comprimento **_n_** - o genoma codificado, que é caracterizada por uma cadeia com caracteres "A", "C", "G", "T" e "?".


* Saída
Se for possível decodificar o genoma, imprima "Segredos desvendados". Se não for possível, imprima "Feiticeiro misterioso" .

* Notas

No primeiro exemplo de teste, os pontos de interrogação do genoma podem ser substituídos por um caractere 'A', um caractere 'T' e um caractere 'G', em qualquer ordem;

No segundo exemplo de teste, o genoma é válido;

No terceiro exemplo de teste, não é possível obter uma quantidade igual de caracteres 'A', T', 'G' e 'C' ao substituir os caracteres possíveis nas posições dos pontos de interrogação no genoma.

* For example:

|Input|Result|
|-----|------|
|8<br>AG?C??CT|Segredos desvendados|
|4<br>AGCT|Segredos desvendados|
|6<br>????G?|Feiticeiro misterioso|
|4<br>AA??|Feiticeiro misterioso|
|4<br>????|Segredos desvendados|
|252<br>???????GCG??T??TT?????T?C???C?CCG???GA???????AC??A???AAC?C?CC??CCC??A??TA?CCC??T???C??CA???CA??G????C?C?C????C??C??A???C?T????C??ACGC??CC?A?????A??CC?C??C?CCG?C??C??A??CG?A?????A?CT???CC????CCC?CATC?G??????????A???????????????TCCCC?C?CA??AC??GC????????|Segredos desvendados|


