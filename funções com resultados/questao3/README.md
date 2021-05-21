# One-Time Pad
Segurança de dados é um assunto muito sério atualmente. Um tipo extremamente simples de cifra, mas que nas condições ideais (virtualmente impossíveis de serem garantidas) é chamado "one-time pad". Ela consiste em cifrar uma mensagem com uma chave aleatória do mesmo tamanho da mensagem. Essa chave só pode ser usada 1 única vez, por isso a cifra é conhecida como "one-time".

A cifra em si é muito simples, como mostrado abaixo. A equação (1) apresenta um processo de encriptação, enquanto que a equação (2) o processo de decifragem.

**cipher_text=plain_text ⊕ key** (1)

**plain_text=cipher_text ⊕ key** (2)

em que ⊕ denota uma operação xor ("ou exclusivo").

Sua tarefa é simples: criar uma função decrypt, que recebe 2 números: um número encriptado, e um número que será usado como chave. Você deve desencriptar o número para descobrir o número original que foi enviado.

* Entrada

A entrada consiste nos parâmetros da função decrypt, dois números inteiros **_a_** e **_b_**.

* Saída

O número **_c_**, plain_text referente à entrada **_a_** (cipher_text) com **_a_** chave **_b_**.

* Observações

No caso de teste 1, usando 255 como número encriptado, e 131 como número chave, descobrimos que o número "em claro" é 124.

Semelhante para os outros casos de teste.

* For example:

Input|Expected
-----|--------
print(decrypt(255,131))|124
print(decrypt(1200, 1243))|107
print(decrypt(12345, 67890))|80139
print(decrypt(151515, 1121))|150458
print(decrypt(346512, 125476))|304052
print(decrypt(252525, 5000))|248293
