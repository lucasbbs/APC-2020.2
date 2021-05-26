# Álgebra linear, não. Matemática.
Cedo ou tarde, você irá perceber que o ramo mais útil da matemática é a álgebra linear. Em alguns lugares, nem sequer utilizam o nome álgebra linear. Usam simplesmente matemática! Neste problema, você irá utilizar um pedacinho bem minúsculo da álgebra linear, voltado para geometria.
Na escola, nós aprendemos a determinar se um par de vetores bi ou tridimensionais é ortogonal (ou seja, se o ângulo entre os vetores é de 90° ) calculando seu produto interno euclidiano:

 **_u_ ⋅ _v_ = _xᵤ_ ⋅ _xᵥ_ + _yᵤ_ ⋅ _yᵥ_**     (para 2 dimensões - bidimensionais) ou
**_u_ ⋅ _v_ = _xᵤ_ ⋅ _xᵥ_ + _yᵤ_ ⋅ _yᵥ_  + _zᵤ_ ⋅ _zᵥ_**     (para 3 dimensões - tridimensionais)

Dois vetores **_u_** e **_v_** são ortogonais se, e somente se, **_u_ ⋅ _v_ = 0**. Neste problema, você deve determinar se um dado par de vetores **_n_**-dimensionais **_u_** e **_v_** é ortogonal.

* Entrada
A primeira linha da entrada contém um único inteiro **_n_ ( 1 ≤ _n_ ≤ 10⁵)**, que indica a dimensão dos vetores a serem lidos, ou seja, o número de coordenadas cartesianas de um vetor.

A segunda linha contém _n_ inteiros **_uᵢ_ (−100 ≤ _uᵢ_ ≤ 100)** separados por espaço, que são as _n_ coordenadas do vetor _u_.

A terceira linha contém _n_ inteiros **_vᵢ_ (−100 ≤ _vᵢ_ ≤ 100)** separados por espaço, que são as _n_ coordenadas do vetor _v_.

* Saída
Se os vetores **_u_** e **_v_** forem ortogonais, imprima a mensagem "ortogonais" (sem aspas duplas). Caso contrário, imprima o valor do produto interno euclidiano entre eles.

* Observação

Para ler as n coordenadas de um vetor em uma única linha, basta utilizar o seguinte código: <pre>vet = list(map(int,input().strip().split()))[:n]</pre>

No primeiro caso de teste, os vetores são ortogonais pois (-3)*1 + (-4)*1 + 2*1 + 5*1 = 0.

* For example:

|Input|Result|
|-|-|
|4<br>-3 -4 2 5<br>1 1 1 1|ortogonais|
|3<br>-2 0 1<br>1 2 -2|-4|
|8<br>1 0 1 0 1 0 1 0<br>0 1 0 1 0 1 0 1|ortogonais|
|3<br>2 -2 1<br>3 2 -2|ortogonais|
|2<br>1 7<br>2 -3|-19|
|1<br>1<br>-2|-2|
