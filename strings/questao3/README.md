# O Valor das Palavras
Um padrão comum de codificação de caracteres é ASCII - confira a tabela ascii aqui. Esse código atribui um valor de 0 até 127 para alguns caracteres comuns, por exemplo o valor ascii para 'A' é 65.

Dado uma string **_s_** diga qual o valor total da string, definido como a soma do valor de cada caractere.

* Entrada

A entrada consiste em uma string **_s_** **(0 ≤ |_s_| ≤ 10⁴ )**. **_s_** é composta por letras, números e símbolos de pontuação.  

* Saída

Imprima o valor de s, definido como a soma dos valores de cada caractere no código ASCII. 

* Observações

No primeiro exemplo de teste, **_s = abc_**. Olhando na tabela, **_a_ = 97**; **_b_ = 98**; **_c_ = 99**, então somamos os valores **97 + 98 + 99 = 294**, que é a resposta.
* For example:

|Input|Result|
|-----|------|
|abc|294|
|abcdefghijklmnopqrstuvwxyz|2847|
|ABCDEFGHIJKLMNOPQRSTUVWXYZ|2015|
|mT;Oobn6KDUSmJG6BlRjR26?;;APfr;.Q?d0a1w,k ivWsQ v9!SUhsC5hgo oDBD6EQ5aLp6!Cdet7IQyNxEg6l?QjLMILk:2NS|7977|
|RwypG!nG1ri7GcQSQQVKTw2Zilz:;Tv6?ubMmP vUN2:1;.I203TC5!2gBgyT.NJbPyItgWG.08JRE9Po9gjQ6tibwnNIz HoO4gAKVPotuGy8U5lCNz0cQvfTFP ,g3bfz!Q68gL!0n0:jO:uUZu!90Qea6rjWDU3na?CyuYHqeBfEGUM;Ic5I00tQkSJl IAaftVh.|16238|
|pu8R:W4:?IUoxeZQsZF7EQ136Iv;eZVtIeMB2oJf9ClxyByJUPoj:qnU8Ajj2 yYWX:p!ra.I1EAywmSDaFiId?KrbiMFKS!B43.la3vc?,YEKF9WZr3:r4sSmtAQ.?:6i5MDjkcj6as9,zOT9rwF6OBHd.bmeElO6qYVr!KaCB440wjY?dAy:crHDlFLs4Ai. F?z1 qMYI8hIJ,c.FEZ3XWkWUkKQU BLAbKygMbx2zN6fhIdhWM8rpC:rXxuCRWOiqueFj7kaqO;Slp1jQysc2 ZXBS0;PLQC5S06rFVS|24643|
