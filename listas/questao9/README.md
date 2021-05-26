# Sala de Espera
Bruna precisa fazer um exame de sangue. Ela chegou no laboratório, e foi pedido que ela espere na sala de espera. Essa sala possui **_m_** fileiras com **_n_** cadeiras cada. **O espaço entre cada cadeira é de 1m**.

Como ainda estamos em pandemia, Bruna gostaria de se sentar o mais distante possível de outras pessoas, mas ela está há muito tempo sem comer, e não consegue mais pensar com clareza para decidir o melhor lugar, então você vai ajudá-la, encontrando o lugar vago em alguma das m fileiras que maximize a distância para qualquer vizinho na mesma fileira.

* Entrada

A primeira linha da entrada possui dois inteiros: **_m_** e **_n_**, o número de fileiras, e a quantidade de cadeiras em cada fileira, respectivamente. **(1 ≤ _m_ ≤ 10 ; 2 ≤ _n_ ≤ 100 )**.

As próximas **_m_** linhas da entrada contém **_n_** inteiros cada, as **_m_** fileiras da sala. Cada fileira é representada por **_n_** inteiros, **_a₀_, _a₁_, ..., _aₙ₋₁_,** onde **_aᵢ_∈{0,1}**. Se **_aᵢ_ = 0** o lugar está desocupado, e Bruna pode se sentar nele. Caso contrário, o lugar está ocupado. É garantido que haverá pelo menos 1 espaço vazio em cada fileira.

* Saída

imprima a maior distância que Bruna pode ficar de qualquer outra pessoa em uma fileira.

* Observações

No primeiro exemplo de teste, a maior distância possível para outra cadeira ocupada ocorre quando Bruna senta na primeira cadeira da primeira fila;

No segundo exemplo de teste, Bruna consegue se sentar, no máximo, a 1 metro de qualquer outra cadeira ocupada.

* For example:

Input|Result
-|-
4 6<br>0 0 0 0 1 1<br>1 1 0 0 0 1<br>0 0 0 1 0 1<br>1 1 0 0 1 1|4
2 12<br>1 0 0 1 0 0 1 1 0 1 0 1<br>1 1 1 1 0 0 1 0 1 0 1 1|1
3 8<br>1 1 1 0 1 1 1 1<br>0 0 0 1 0 1 0 1<br>0 1 1 0 1 1 0 1|3
2 55<br>0 1 1 1 0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 1 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 1 0 1 1 1 1 0 0 0 1 1 0 0 1 1 0 1 1 1 1<br>1 0 0 0 1 0 1 1 1 0 0 0 1 1 1 0 0 0 0 1 1 1 0 0 1 1 1 1 0 0 1 0 0 1 1 0 1 1 0 0 0 1 0 0 0 1 0 1 1 1 1 0 0 1 1|4
1 47<br>0 0 0 0 1 0 0 0 0 1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 1 0 0 1 0 1 1 1 0 1 1 1 0 1 0 1 1 0 1 0 0 1 1|4
3 82<br>1 1 0 1 0 1 0 1 0 0 1 0 1 1 0 0 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 0 1 0 0 0 0 1 1 0 0 1 0 0 0 1 0 0 1 0 1 0 0<br>1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 1 0 1 1 1 0 1 1 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 1 1 1 1 0 1 0 0 1<br>1 1 0 0 0 0 0 1 0 0 0 1 1 0 1 0 0 0 1 0 0 1 0 0 1 1 1 0 1 1 0 0 1 1 0 1 0 0 0 1 1 1 1 0 0 0 0 0 0 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 0 0 1 1 0 0 0 1 0 1 1 1 1 1 1 1 0 1|3
