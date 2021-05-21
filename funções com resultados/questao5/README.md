# Divisão por Zero
Em épocas de aulas remotas, o professor Marco, que é muito solícito e brincalhão, estava ensinando a seus alunos sobre divisão de inteiros e recebeu a seguinte pergunta:

<pre>prof, pq não da pra dividir por zero?

porque aí eu te quebro na porrada
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk</pre>

Como toda a turma se divertiu com a resposta do professor Marco, ele pediu a sua ajuda para escrever uma função chamada divisao(a,b), que retorne o quociente e o resto da divisão de a por b ou "Te quebro na porrada" caso o valor de b seja zero.



* Entrada
A função possui dois parâmetros **_a_** e **_b_** inteiros em que **0 ≤ _a_, _b_ ≤ 10⁹**.



* Saída
A função deve retornar dois inteiros que representam o quociente e o resto da divisão ou "Te quebro na porrada" caso o valor de b seja zero.


* Observações
Submeta somente o que foi solicitado.

No primeiro exemplo de teste, **_a_= 8** e **_b_= 2**, logo **8 ÷ 2 = 4** e  **8 % 2 = 0**.

No segundo exemplo de teste, **_a_** **= 42**, mas como **_b_ = 0**, teremos uma divisão por zero. Assim não é possível calcular a divisão,e "Te quebro na porrada" deve ser retornado.

No terceiro exemplo de teste, **_a_= 7** e **_b_= 4**. Deve-se retornar **7 ÷ 4 = 1 e 7 % 4 = 3**.
Para uma função retornar dois valores, durante o uso do return, deve-se separar cada um dos valores ou variáveis por vírgula, exemplo:

<pre>
def dobraetriplica(a):
  dobro = 2*a
  triplo = 3*a
  return dobro, triplo
  </pre>

Particularidade do Tópico
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).


For example:

Input|Expected
-----|--------
print(divisao(8, 2))|(-4,0)
print(divisao(42, 0))|Te quebro na porrada
print(divisao(7, 4))|(-1,3)
print(divisao(25, 7))|(-3,4)
print(divisao(1337, 25))|(-53,12)
print(divisao(0, 0))|Te quebro na porrada
