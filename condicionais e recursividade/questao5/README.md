# Seu Pimenta
O buffet de Seu Pimenta é muito famoso na cidade onde mora e, por isso, seus serviços são muito solicitados nos eventos locais. Nos últimos dias, devido à realização de vários eventos em um mesmo dia, Seu Pimenta encontrou dificuldades para orientar adequadamente seus funcionários. Como resultado, Seu Pimenta têm notado que alguns talheres "sumiram" ou que não foram corretamente organizados e armazenados, deixando o depósito e o armário de talheres bastante bagunçado.

Recentemente, Seu Pimenta recebeu uma proposta para preparar um banquete para uma conferência famosa, que receberá muitas pessoas de fora da cidade. Considerando os últimos fatos relacionados aos talheres do buffet, Seu Pimenta deixou claro ao cliente que não tem talheres suficientes para atender todos os participantes. No entanto, confiando em Seu Pimenta e na sua alta credibilidade na cidade, o cliente solicitou seus serviços mesmo assim e Seu Pimenta agora tem que correr para organizar mais um buffet.

Seu Pimenta consultou o depósito e verificou que existiam números diferentes de garfos , facas e colheres. Para maximizar a quantidade de pessoas que conseguirão jantar, Seu Pimenta estabeleceu que cada pessoa seria capaz de jantar se possuísse um par de garfo e faca, ou uma colher. Ajude Seu Pimenta e elabore uma função chamada quantosJantam(n, g, f, c) que calcule a maior quantidade possível de pessoas presentes no banquete que conseguiriam jantar de acordo com a estratégia proposta.

* Entrada
Os parâmetros da função são quatro inteiros **_n_**, **_g_**, **_f_**, **_c_** ≥ 0 indicando, respectivamente, a quantidade de pessoas existentes no banquete, a quantidade de garfos, a quantidade de facas e a quantidade de colheres.

* Saída
Imprima um valor inteiro indicando a maior quantidade possível de pessoas presentes no banquete que conseguirão jantar.

* Observações
Submeta somente o que foi solicitado.

No primeiro exemplo de teste, pode-se formar apenas um jogo de garfo e faca, para uma pessoa comer. Ademais, 4 colheres possibilitam que outras 4 pessas possam comer. No total, 5 pessoas conseguirão comer no banquete.
No segundo exemplo de teste, pode-se formar dois jogos de garfo e faca, possibilitando que duas pessoas possam comer. Como existem 2 colheres, outras 2 pessas conseguem comer. No total, 4 pessoas conseguirão comer no banquete.
No terceiro exemplo de teste, não é possível formar um jogo de garfo e faca, mas como existem 7 colheres, 7 pessoas conseguirão comer no banquete.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
* For example:

Input|Expected
-----|--------
quantosJantam(10, 3, 1, 4)|5
quantosJantam(15, 2, 5, 2)|4
quantosJantam(12, 0, 1, 7)|7
quantosJantam(20, 22, 4, 10)|14
quantosJantam(10, 5, 5, 12)|10
quantosJantam(0, 444, 213, 333)|0
