# Lirou Bob
Lirou Bob, o filho de Dêivis, é muito novo e não sabe como contar, hoje em dia ele sempre conta primeiro todos os números ímpares menores ou iguais que **_n_** e depois os pares menores ou iguais que **_n_**, em ordem crescente. Dessa forma, dado um número **_n_**, ajude Dêivis a saber qual o k-ésimo número que Bob irá contar. Para essa tarefa, implemente a função **k_esimo(n, k)**.

* Entrada
Os parâmetros da sua função serão os inteiros 1 ≤ k ≤ n ≤ 10¹².


* Saída
A função deve retornar o k-ésimo número que Bob irá contar.


* Observações

No primeiro teste, se Lirou Bob fosse contar até o número **8**, ele iria realizar a contagem da seguinte forma: **1,3,5,7,2,4,6,8**. Portanto, o sexto número que Marquito irá contar é o número **4**.

No segundo teste, se Lirou Bob fosse contar até o número **10**, ele realizaria a contagem da seguinte forma: **1,3,5,7,9,2,4,6,8,10**. Portanto, o nono número que Marquito irá contar é o número **8**.

No terceiro teste, se Lirou Bob fosse contar até o número **7**, ele realizaria a contagem da seguinte forma: **1,3,5,2,4,6,7**. Portanto, o primeiro número que Bob irá conta é o número **1**.

Submeta somente o que foi solicitado.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


* For example:

Input|Expected
-----|--------
print(k_esimo(8, 6))|4
print(k_esimo(10, 9))|8
print(k_esimo(7, 1))|1
print(k_esimo(6, 6))|6
print(k_esimo(45, 30))|16
print(k_esimo(50, 5))|9

