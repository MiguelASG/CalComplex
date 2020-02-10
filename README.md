# CalComplex
## Esta libreria de python trabaja con numeros complejos, y los representa como una lista o tupla de dos posiciones (de esta forma por ejemplo[1,3]), la primera posicion es la parte real y la segunda la parte compleja. 
## Para trabajar con la libreria tendremos los siguientes tipos a entrar:
### 1. C, cuando se indica que recibe o retorna este tipo de variable se refiere a un complejo de la forma antes descrita, por ejemplo [4,1].
### 2. E, cuando se indica que recibe o retorna este tipo de variable, se refiere a un escalar real por ejemplo 3.
### 3. V, cuando se indica que entra o retorna este tipo de variable, se refiere a una vector de complejos de tamaño n, por ejemplo [[1,1],[3,5]].
### 4. M, cuando se indica que entra o retorna este tipo de variable, se refiere a una matriz de complejos de tamaño nxm, por ejemplo [[[1,1],[3,5]],[[2,1],[4,1]]]
### 5. ang, cuando se indica que entra o retorna este tipo de variable, se refiere a un angulo en grados, donde el angulo es igual o mayor a 0, por ejemplo 90.
 
## La libreria cuenta con las siguientes funciones:

## Suma de numeros complejos:
### suma dos numeros complejos.
### suma(C,C) retorna un C.

## Producto de numeros complejos:
### multiplica dos numeros complejos.
### mult(C,C) retorna un C.

## Resta de numeros complejos:
### resta dos numeros complejos.
### resta(C,C) retorna un C.

## División de numeros complejos:
### divide dos numeros complejos.
### div(C,C) retorna un C.

## Módulo de un numero complejo:
### saca el modulo de un numero complejo.
### mod(C) retorna un E.

## Conjugado de un numero complejo:
### conjuga un numero complejo.
### conj(C) retorna un C

## Conversión entre representaciones polar y cartesiano de un numero complejo
#### dado un numero complejo, retorna la representacion polar, y dando la representacion polar da el numero complejo:
### Complejo a Polar:
#### pol(C) retorna [E,ang].
### Polar a Complejo:
#### cart(E,ang) retorna un C.


## fase de un número complejo:
### halla la fase de un numero complejo:
### fase(C) retorna un E.

## Adición de vectores complejos.
### Suma dos vectores complejos.
### sumvect(V,V) retorna un V.

## Inverso (aditivo) de un vector complejo.
### halla el inverso aditivo de un vector complejo.
### invect(V) retorna un V.

## Multiplicación de un escalar por un vector complejo.
### multiplica un escalar por un vector complejo.
### escxvec(E,V) retorna un V.

## Adición de matrices complejas.
### Suma dos matrices complejas.
### sumatriz(M,M) retorna un M.

## Inversa (aditiva) de una matriz compleja.
### halla el inverso aditivo de una matriz compleja.
### invmatriz(M) retorna un M.

## Multiplicación de un escalar por una matriz compleja.
### multiplica un escalar por una matriz compleja.
### escxmat+r(E,M) retorna un M.

## Transpuesta de una matriz/vector
### transpone una matriz o un vector.
### traspuesta(M) retorna un M.

## Conjugada de una matriz/vector
### halla la conjugada de una matriz o un vector complejo.
### conjmv(M) retorna un M.

## Adjunta (daga) de una matriz/vector
### halla la adjunta de una matriz compleja.
### adjunta(M) retorna un M.

## Producto de dos matrices (de tamaños compatibles)
### halla el producto de dos vectores complejos.
### mulmatr(M,M) retorna un M.

## Función para calcular la "acción" de una matriz sobre un vector.
### halla el accion entre una matriz y un vector de numeros complejos.
### accion(M,V) retorna un M.

## Producto interno de dos vectores
### halla el producto interno entre dos vectores de numeros complejos.
 ### innervec(V,V) retorna un C.

## Norma de un vector
### halla la norma de un vector de numeros complejos.
### norma(V) retorna un R.

## Distancia entre dos vectores
### halla la distacia entre dos vectores de numeros complejos.
### distanciavec(V,V) retorna un R.

## Revisar si una matriz es unitaria
### comprueba si una matriz de numeros complejos es unitaria.
### matuni(M) retorna un bool(True o False).

## Revisar si una matriz es Hermitiana
### comprueba si una matriz de numeros complejos es hermitiana.
### hermitian(M) retorna un bool(True o False).

## Producto tensor de dos matrices/vectores
### halla el producto tensor de dos vectores complejos.
### protens(M,M) retorna una M.
