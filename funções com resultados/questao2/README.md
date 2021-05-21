# Doces
Os amigos Rofera e Loffera estão brigando e você tem que resolver. Existem n fichas de sinuca e você quer distribuí-las entre os dois amigos de um modo que:

Loffera irá receber **_a_ (_a_ > 0)** fichas;
 
Rofera irá receber **_b_ (_b_ > 0)** fichas;
 
Cada amigo irá receber um número inteiro de fichas;

Rofera irá receber mais fichas do que Loffera **(_b_ > _a_)**;

Todas as fichas vão ser dadas para um dos dois amigos **(_a_ + _b_ = _n_)**;

Sua tarefa é calcular o número de modos de distribuir exatamente _n_ fichas entre os amigos respeitando as regras acima. Para isso, implemente a função sinuquera(n).

* Entrada
O único parâmetro da sua função será o valor **_n_ ≥ 1**.


* Saída
A função deve retornar o número de modos de distribuir exatamente n fichas entre os amigos, respeitando as regras acima.

* Observações
Submeta somente o que foi solicitado no enunciado da questão.

* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

Input|Expected
-----|--------
print(sinuquera(7))|3
print(sinuquera(1))|0
print(sinuquera(456))|227
print(sinuquera(2000000000))|999999999
print(sinuquera(763243547))|381621773
print(sinuquera(98))|48
