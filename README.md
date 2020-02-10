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
### dado un numero complejo, retorna la representacion polar, y dando la representacion polar da el numero complejo:
## Complejo a Polar:
### pol(C) retorna [E,ang].
## Polar a Complejo:
### cart(E,ang) retorna un C.


## fase de un número complejo:
### halla la fase de un numero complejo:
### fase(C) retorna un E.
