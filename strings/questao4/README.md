# Senha válida
Dêivis está montando um site de E-Commerce, mas antes de começar, ele percebeu que precisaria de um validador de senhas para conseguir validar as senhas dos usuários. Como Dêivis não é um profissional em segurança, ele pediu que você faça o validador de senhas!

Para uma senha ser segura, ela precisa dos seguintes requisitos:

Ela deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um caractere numérico;
Ela não pode ter nenhum caractere de pontuação, acentuação ou espaço;
Ela pode ter entre 6 e 32 caracteres (inclusivo).

* Entrada

A entrada contém uma linha com uma string s (1≤|s|≤100), que é a senha que precisa ser verificada.

* Saída

A saída contém uma linha, que pode ser “Senha valida.” (sem aspas duplas), caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.” (sem aspas duplas), se um ou mais requisitos não forem atendidos.

* Observações

No primeiro exemplo de teste, "AbcdEfgh99", a senha contém pelo menos um caractere minúsculo, um caractere maíúsculo, e pelo menos um número. Além disso, possui tamanho maior ou igual a 6 e menor ou igual a 32. Assim, a senha é válida.
No segundo exemplo de teste, "Aass9", a senha é inválida, pois seu tamanho é menor do que 6 caracteres.
No terceiro exemplo de teste, "cFa3!rW9", a senha é inválida, pois possui um caractere ('!') de pontuação.

* For example:

|Input|Result|
|-----|------|
|AbcdEfgh99|Senha valida.|
|Aass9|Senha invalida.|
|cFa3!rW9|Senha invalida.|
|fwPjH9zyQKXfSx9A|Senha valida.|
|r-nU[=2!BQU'w4g<|Senha invalida.|
|B3LBaXYM45Re8YXmP7WXu3RKTMU6rtDTVgqhkh8Ja|Senha invalida.|
