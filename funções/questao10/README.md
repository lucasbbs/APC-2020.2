# Pacotes de bolacha v2
O prof. Fagundes comprou uma caixa com _m_ pacotes de bolacha recheada para distribuí-los igualmente entre os _n_ alunos da sua turma de Estruturas de Dados na Universidade de Brasília (UnB). Apesar dos alunos terem adorado essa surpresa, cada um consegue comer no máximo _k_ pacotes de bolacha, portanto, alguns desses pacotes entregues por aluno podem sobrar. A generosidade do querido professor é tamanha, tanto que ele pretende pegar esses pacotes restantes e entregá-los aos funcionários do Departamento de Ciência da Computação (CIC) da UnB.

Sabendo-se que cada aluno sempre recebe e come ao menos um pacote de bolacha, elabore uma função chamada  pacotesDeBolacha que receba os três números inteiros _m_, _n_ e _k_ como parâmetros e imprima a quantidade máxima de pacotes de bolacha que o prof. Fagundes entregará aos alunos da sua turma.

* Entrada
Não há entrada de dados. A função é chamada para valores arbitrários definidos nos casos de teste que são três números inteiros _m_, _n_ e _k_  (1 ≤ _n_ ≤ 10⁴, _n_ ≤ _m_ ≤ 10⁴, 1 ≤ _k_ ≤10⁴ ) associados ao número total de pacotes de bolacha, a quantidade de alunos da turma e quantos pacotes de bolacha cada aluno dessa turma consegue comer, respectivamente.

* Saída
A função pacotesDeBolacha deve imprimir a quantidade máxima de pacotes de bolacha que o prof. Fagundes entregará aos alunos da sua turma, respeitando as restrições descritas no enunciado.

* Observação 
Submeta somente o que foi solicitado. Não é necessário validar se os números estão dentro do intervalo definido.

No primeiro caso de teste, existem 4 pacotes de bolacha, 4 alunos e cada aluno consegue comer um pacote de bolacha, totalizando 4 pacotes.
No segundo caso de teste, existem 13 pacotes de bolacha e 5 alunos, sendo que cada aluno consegue comer _k_ = 2 pacotes de bolacha. Assim, tentando dividir igualmente os 13 pacotes para os 5 alunos, temos que cada aluno poderia comer 2 pacotes, o que é possível de acordo com _k_. Assim, a turma toda comerá 10 pacotes.
No terceiro caso de teste, existem 10 pacotes de bolacha e 9 alunos, sendo que cada aluno consegue comer _k_ = 2 pacotes de bolacha. A divisão igualitária dos pacotes entre os alunos diz que cada aluno come 1 pacote de bolacha, resultando em 9 pacotes para toda a turma.
* Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, por esse critério, caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

* For example:

|Input|Expected
|-----|--------
|pacotesDeBolacha(4,4,1)|4
|pacotesDeBolacha(13,5,2)|10
|pacotesDeBolacha(10,9,2)|9
|pacotesDeBolacha(60,20,3)|60
|pacotesDeBolacha(4,4,1)|4
|pacotesDeBolacha(23,6,6)|18

