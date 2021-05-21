# Operações com strings
Faça um programa que leia duas strings e um número inteiro, e faça as operações de (1) concatenação das duas strings, (2) repetição da primeira string pelo número inteiro de vezes, e (3) ambas operações juntas. A função concatenar deve receber como parâmetro as duas strings. A função repetir deve receber a primeira string e número inteiro de repetições. Por fim, a função ambos deve receber as duas strings e o número inteiro de repetições.

* Entrada

A entrada contém duas strings e um número inteiro positivo separados por espaço str1,str2,a | a>0.

* Saída

A saída deve ser composta de 3 linhas, cada uma como apresentada a seguir.

A concatenação da primeira string com a segunda;
A repetição da primeira string com o número inteiro;
A repetição da string resultante da concatenação da primeira string com a segunda pelo número inteiro de vezes, conforme os exemplos.
* Particularidade do Tópico
* Atenção, a criação de funções com os nomes determinados pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos, caso as criações não tenham sido feitas corretamente (sendo case-sensitive o nome de cada função).

* For example:

Input|Expected
|-----|--------
|Alo Oi 5 |AloOi
|  |AloAloAloAloAlo
|  |AloOiAloOiAloOiAloOiAloOi 

Input|Expected
|-----|--------
|Eu CurtoStrings 3 |EuCurtoStrings
| |EuEuEu
| |EuCurtoStringsEuCurtoStringsEuCurtoStrings 

Input|Expected
|-----|--------
|Mamao Papaia 1 |MamaoPapaia
||Mamao
||MamaoPapaia

|Input|Expected
|-----|--------
|DaleDo DeleDo 12 |DaleDoDeleDo
||DaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDoDaleDo
||DaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDoDaleDoDeleDo 

Input|Expected
|-----|--------
|XesqueDo DesqueDo 30 |XesqueDoDesqueDo
||XesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDoXesqueDo
||XesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDoXesqueDoDesqueDo 

|Input|Expected
|-----|--------
|EUAMO APC 44 |EUAMOAPC
||EUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMOEUAMO
||EUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPCEUAMOAPC 



