# Escolha Premiada
Você foi convidado para a chance ÚNica de Brindes do programa do Saustão. Esse jogo funciona da seguinte maneira, você vai receber uma lista de possíveis prêmios que poderá ganhar e cada um terá o seu respectivo valor. Depois de ver todos os prêmios, Sausto Filva irá sortear um valor para você. Se você conseguir escolher um número de brindes cujo a soma do valor desses brindes seja igual ao valor sorteado, você ganha todos os brindes, senão perde tudo. Como você já sabe como o jogo funciona e é um exímio programador, você resolveu implementar um programa para dizer se é possível escolher um conjunto de brindes que o faça ganhar o prêmio ou não.



* Entrada
A entrada contém 2 linhas. A primeira linha contém **_n_** inteiros **_v_** onde cada **_vᵢ_** indica o valor de um dos prêmios da lista **(0 ≤ _vᵢ_ ≤ 100000 e 1 ≤ _n_ ≤ 20)**.

A segunda linha contém um inteiro que indica o número **_s_** sorteado por Sausto **(1 ≤ _s_ ≤ 2000000)**.



* Saída
A saída deve conter a frase 'E possivel ganhar.', se for possível ganhar os prêmios e 'Impossivel ganhar.' se não for possível ganhar os prêmios.

* Notas

No primeiro exemplo de teste, os brindes 2 e 4 possuem valores iguais a 2 e 8 que, somados, são iguais ao número sorteado;

No segundo exemplo de teste, nenhuma combinação possível dos valores dos brindes disponíveis resulta em uma soma igual ao número sorteado por Saustão.

Input|Result
-|-
1 2 3 8<br>10|E possivel ganhar.
1 2 3 8<br>7|Impossivel ganhar.
2 2 2 2 5 2 2<br>15|E possivel ganhar.
8 0 9 8 5<br>17|E possivel ganhar.
4 5 7 8 7<br>10|Impossivel ganhar.
2 9 9 2 10 2 18 14<br>27|E possivel ganhar.

