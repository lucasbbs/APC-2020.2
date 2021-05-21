# Irmão mais velho v2
O MMORPG mais famoso do momento, Instant Soul Crushing (ISC), permite que seus jogadores realizem duelos entre si sob o sistema RISCU. Este sistema recebe o nível de poder dos dois jogadores e diz qual jogador é o ganhador e qual jogador é o perdedor.

Você, como um membro de ISC,  deve implementar o sistema RISCU: escreva uma função chamada riscu(powerA, powerB) que receberá o poder dos jogadores A e B e deverá imprimir: 

Se o jogador A for mais forte: Jogador A vence   
Se o jogador B for mais forte: Jogador B vence 
Se ambos jogadores têm a mesma força: Dois jogadores igualmente fracos
* Entrada
A entrada consiste de dois inteiros _powerA_,_powerB_ que indicam os poderes dos jogadores A e B, respectivamente.

* Saída
A saída deve conter a frase Jogador A vence se o jogador A for mais forte, Jogador B vence se o jogador B for mais forte ou Dois jogadores igualmente fracos se ambos jogadores possuem a mesma força.

* Observações
Submeta somente o que foi solicitado.

* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

Input|Expected
-----|--------
riscu(5, 10)|Jogador B vence
riscu(7231, 4442)|Jogador A vence
riscu(457278, 457278)|Dois jogadores igualmente fracos
riscu(-10, 10)|Jogador B vence
riscu(-444, -445)|Jogador A vence
riscu(-211442, 0)|Jogador B vence
