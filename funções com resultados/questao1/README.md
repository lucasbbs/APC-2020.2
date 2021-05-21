# Quanto Falta?
Seu amigo Paco está fazendo a matéria Ultimate Frisbee. Ele achou que seria uma matéria fácil para conseguir alguns créditos, mas surpresa! A matéria na verdade tem 3 provas, com pesos diferentes. A nota final é dada como a média ponderada das três provas, ou seja:

![equation](http://www.sciweavers.org/tex2img.php?eq=media%5C_final%20%3D%20%20%5Cfrac%7Bn_1%20%20%20p_1%20%2B%20n_2%20%20%20p_2%20%2B%20n_3%20%20p_3%7D%7Bp_1%20%2B%20p_2%20%2B%20p_3%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

onde **_nᵢ_**, é a nota na iésima nota, que tem peso pi.

Ele já fez 2 das 3 provas, e pediu sua ajuda para descobrir quanto precisa tirar na terceira para conseguir a menção que gostaria. Faça uma função nota que vai retornar quanto Paco precisa tirar na terceira prova.

* Entrada

A entrada consiste nos parâmetros da função nota. A função recebe 6 parâmetros, nessa ordem:

3 números inteiros **_p_** **₁**, **_p_** **₂**, e **_p_** **₃**, os pesos de cada uma das 3 provas, seguidos de
1 string **_s_**, a menção que Paco gostaria. **_m_** pode ter 3 valores: 'MM', 'MS' ou 'SS'. Seguido de
2 números float, _n1_ e _n2_, as notas que Paco tirou nas primeiras 2 provas.
* Saída

Sua função deve retornar quanto falta para Paco atingir a média que espera. Note que esse valor pode ser maior do que 10 (o valor máximo de uma prova). Esse valor também pode ser negativo, o que significa que Paco já atingiu a menção que queria.

* Observações

No primeiro caso de teste, o resultado é 5.0, porque todas as prova tem o mesmo peso. Paco tirou 5 nas duas primeiras, se tirar 5 na última sua média final será dada por: ![equation](http://www.sciweavers.org/tex2img.php?eq=media%5C_final%20%3D%20%5Cfrac%7B5%20%2B%205%20%2B%205%7D%7B3%7D%20%3D%20%5Cfrac%7B15%7D%7B3%7D%20%3D%205&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0), a nota para MM.
No segundo caso de teste, a situação é semelhante ao caso 1, mas Paco quer um MS, cujo mínimo é 7.0. Nesse caso, ele precisa de 11 na prova final, pois ![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B5%20%2B%205%20%2B%2011%7D%7B3%7D%20%3D%20%5Cfrac%7B21%7D%7B3%7D%20%3D%207&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0).
O terceiro caso é semelhante ao segundo, mas como a prova final tem peso maior que as outras, ainda é possível conseguir o MS.
Submeta somente o que foi solicitado no enunciado da questão.
Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print(nota(1, 1, 1, 'MM', 5, 5))|5.0
print(nota(1, 1, 1, 'MS', 5, 5))|11.0
print(nota(1, 1, 2, 'MS', 5, 5))|9.0
print(nota(1, 2, 3, 'SS', 7.4, 8.3))|10.0
print(nota(2, 2, 4, 'SS', 9.4, 9.0))|8.8
print(nota(1, 2, 4, 'MM', 9.5, 9.0))|1.875
