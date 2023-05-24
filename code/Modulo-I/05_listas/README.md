# Ejercicios de ciclos

# 01 cuenta pares e impares
## Tema: Listas

Diseña e implementa un programa que determine la cuenta de valores pares e impares de los elementos de una lista de números enteros que recibirá en su entrada. Los valores los introduce el usuario uno por uno, se van almacenando en una lista y posteriormente se analizará la lista para determinar cuantos valores pares e impares posee. Consideramos al 0 como par.

## Entrada
Cero o más valores enteros, uno en cada renglón. Finaliza la captura con un *.

## Salida
Se despliega el número de pares e impares que tiene la lista con el siguiente formato: 
PARES=3 o IMPARES=2 cada uno en un renglón. 
El desplegado de la salida consiste en la palabra PARES seguida de un = y luego un número que representa el número de pares en la lista; posteriormente la palabra IMPARES, seguida de un = y luego el número que representa el número de impares que hay en la lista. Cada mensaje en un renglón y en ese orden.

## Ejemplo de ejecución del programa
### Entrada
```
>>> 6
>>> 0
>>> 1
>>> 2
>>> *
```
### Salida
```
PARES=3
IMPARES=1
```
### Entrada
```
>>> *
```
### Salida
```
PARES=0
IMPARES=0
````
-------------------------------------------------
# 02 Sublista pares impares

Desarrolla un programa que, a partir de una lista de números enteros que recibirá del usuario, permita crear y desplegar dos sublistas, una sublista con valores pares y otra sublista con valores impares. 

## Entrada
Cero o más valores enteros, uno en cada renglón. Finaliza la captura con un *

## Salida
Se muestra una salida tal como se ilustra a continuación:
```
PARES
[2, 4, 8]
IMPARES
[1, 5]
```
La palabra PARES en mayúscula en un renglón y posteriormente el despliegue la lista de pares y de manera similar los impares, tal como se muestra en el ejemplo. Respeta el orden y no uses letreros para solicitar las entradas de datos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 2
>>> 4
>>> 1
>>> 8
>>> 5
>>> *
```
### Salida
```
PARES
[2, 4, 8]
IMPARES
[1, 5]
```
### Entrada
```
>>> *
```
### Salida
```
PARES
[]
IMPARES
[]
```
-------------------------------------------------
# 03 Pares y posición
Escribe un programa que primero lea la cantidad de elementos que vas a ingresar en la lista y después acepte cada uno de los elementos. Todos los datos que se ingresan deben ser números enteros.
Posteriormente, el programa debe revisar la lista, y para cada uno de los valores pares que encuentre mostrar un mensaje con la posición y el valor del número par usando un formato que se describe más adelante.

## Entrada
Un número entero que representa la cantidad de valores que tiene la lista, asi como cada uno de los valores de la lista.

## Salida
Un mensaje para cada uno de los números pares encontrados en la lista. El mensaje debe tener el formato:
```
pos XX, valor XX
```
Observa que va la palabra ``pos`` seguida de un ``número``, después una ``coma``, un `espacio`, luego la palabra ``valor`` y luego otro ``número``. 
 
## Ejemplo de ejecución del programa:
### Entrada
```
>>>5
>>>1
>>>2
>>>3
>>>4
>>>5
```
### Salida
```
pos 1, valor 2
pos 3, valor 4
```
-------------------------------------------------
# 04 Lista sin duplicados

Escribe un programa que reciba del usuario una lista, la despliegue y despliegue otra lista con los elementos de la lista original, pero sin elementos duplicados. 

## Entradas
Se recibe un número entero positivo mayor a cero correspondiente al número de elementos que el usuario ingresará.
Se reciben uno a uno y por renglón, los elementos de la lista (strings o numeros de acuerdo al número recibido anteriormente). No uses letreros para solicitar los datos al usuario.

## Salidas
Si el valor correspondiente al número de elementos que tendrá la lista es ```0``` o ```negativo``` se deberá mandar el mensaje ```“Error”```. Si el valor recibido es mayor a 0, se despliega la lista original (después de haber recibido los datos). Posteriormente se despliega la lista sin duplicados.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 4
>>> Pedro
>>> Gerardo
>>> Hugo
>>> Pedro
```
### Salida
```
['Pedro', 'Gerardo', 'Hugo', 'Pedro']
['Pedro', 'Gerardo', 'Hugo']
```
### Entrada
```
>>> 0
```
### Salida
```
"Error"
```

-------------------------------------------------
# 05 Serie Fibonacci

Diseña y codifica un programa en Python que lea la cantidad de n elementos que desea tener en la lista.
El programa debe validar que n sea mayor o igual que 0, de lo contrario lo vuelve a solicitar. Como resultado, se debe desplegar la lista con los primeros n elementos de la serie de Fibonacci.

## Entrada
Un número entero positivo que corresponde al número de términos de la serie de Fibonacci que queremos en la lista. Si el dato recibido es menor que 0, se debe volver a solicitar.

## Salidas
La lista con el número de términos de la serie de Fibonacci solicitados, uno por renglon. No uses letreros para solicitar los datos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 5
```
### Salida
```
[0, 1, 1, 2, 3]
```
### Entrada
```
>>> 9
```
### Salida
```
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```
### Entrada
```
>>> 0
```
### Salida
```
[ ]
```

-------------------------------------------------
# 06 Mezcla y ordena listas

Desarrolla un programa que permita obtener una lista ordenada de menor a mayor a partir de dos listas. Los valores individuales de las listas de entrada los captura el usuario uno por uno y posteriormente se unen ambas listas para obtener una sola lista ordenada de menor a mayor.

## Entradas
Cero o más valores enteros, uno en cada renglón por cada lista. Finaliza la captura de cada lista individual con un *.

## Salidas
Se despliegan las dos listas iniciales y la lista final ordenada con el siguiente formato mostrado en el ejemplo.

## Ejemplo de ejecución del programa
### Entrada
```
>>>3
>>>1
>>>4
>>>5
>>>*
>>>2
>>>9
>>>6
>>>1
>>>3
>>>*
```
### Salida
```
L1=
[3, 1, 4, 5]
L2=
[2, 9, 6, 1, 3]
LORDENADA=
[1, 1, 2, 3, 3, 4, 5, 6, 9]
```
### Entrada
```
>>> *
>>> *
```
### Salida
```
L1=
[]
L2=
LORDENADA=
[]
```

-------------------------------------------------
# 07 Matriz de numeros consecutivos
Escribe un programa que cree una matriz de n filas y m columnas y la llene por números consecutivos por renglón comenzando con el valor 1.

## Entradas
Dos números enteros mayores o iguales a 2 que representarán el numero de renglones n (número de listas) y el número de columnas m (numero de elementos en cada lista), en ese orden. Si alguno de los números recibidos no es mayor o igual a 2, se despliega el mensaje "Error"

## Salida
La matriz de nxm llena con números consecutivos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 3
>>> 2
```
### Salida
```
[ [1, 2], [3, 4], [5, 6] ]
```
### Entrada
```
>>> 3
>>> 3
```
### Salida
```
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
```
### Entrada
```
>>> 1
>>> -3
```
### Salida
```
Error
```

-------------------------------------------------
# 08 Determinante
Desarrolla una función en Python que reciba  una matriz de números enteros de tamaño 2x2 y calcule su determinante.
El determinante de una matriz es un número real asociado a una matriz cuadrada. 
Para una matriz de tamaño 2x2 el determinante se calcula de la siguiente forma:
 | a   b |
 | c   d |
det = a*d - c*b
El programa debe construir la matriz y posteriormente calcular el determinante con la función desarrollada. <b> Utiliza el archivo que encontrarás en el entorno.</b>

En caso de que la matriz no corresponda a una matriz de 2X2 deberá desplegar el mensaje "La matriz no es una matriz de 2x2".
Nota: Se debe incluir una función auxiliar que pida por teclado los valores de los dos renglones de la matriz y la cree. 

Entrada: <br>
Los renglones de la matriz, separando los valores por espacios. (2 valores por renglón, 2 renglones)
Se sugiere utilizar la función <b>split</b> para generar una lista a partir de los datos dados en cada renglón.<br>

Salida: <br>
El valor correspondiente al determinante de la matriz.  En caso de entradas erróneas el mensaje "La matriz no es una matriz de 2x2".<br>

Ejemplo de ejecución del programa<br>
```
>>> 1 2
>>> 3 4
-2

>>> 1 2 1
>>> 1 2 4

La matriz no es una matriz de 2x2
```

-------------------------------------------------
# 09 Cantidad de pares por renglón

Desarrolla una función que reciba una matriz de números enteros y regrese como valor de retorno una lista con la cantidad de números pares que se encuentran en cada renglón.

El programa deberá de leer los datos: cantidad de renglones y columnas y los datos de la matriz. Llamar a la función, la cual le regresará una lista con la cantidad de valores pares en cada renglón y mostrar la lista. 

Entrada <br>
Número de renglones de la matriz
Número de columnas de la matriz
Los datos de la matriz que son números enteros

Salida<br>
Una lista que contiene la cantidad de valores pares de cada renglón de la matriz

Ejemplos de ejecución del programa:<br>
```
>>>3   <--- cantidad de renglones
>>>2   <--- cantidad de columnas
>>>3   <--- datos de la matriz
>>>1
>>>3
>>>8
>>>7
>>>5
[0, 1, 0]
```

-------------------------------------------------
# 10 Suma columnas 

Escribe un programa que pregunte el número de renglones y número de columnas de una matriz, después pregunte cada número de la matriz y regrese una lista con la suma de cada columna de la matriz.
<b>Utiliza el archivo que se te provee en el entorno para implementar tu ejercicio </b>

Entrada:<br>
Dos números enteros que son el número de renglones y el número de columnas, uno por renglón y en ese orden.
La cantidad de números enteros que corresponderán a los elementos de la matriz, en total la cantidad de números a recibir es la multiplicación de los dos primeros números recibidos.

Salida:<br>
Lista con la suma de cada columna de la matriz. 
Si alguno de los números recibidos correspondientes a la cantidad de renglones o de columnas son menores a 1, desplegar el mensaje: "Error".

Ejemplo de ejecución del programa
```plaintext
>>> 3
>>> 1
>>> 2
>>> 4
>>> 5
[11]

>>> 0
>>> 4
Error

>>> 2
>>> 2
>>> 4
>>> -1
>>> 3
>>> 6
[7 5]
```
-------------------------------------------------
# 11 Diagonal principal 
Desarrolla una función que reciba una matriz de números enteros y regrese como valor de retorno una lista con los elementos de la diagonal principal (como lista). <br><br>

El programa deberá de leer los datos: cantidad de renglones y columnas y los datos de la matriz. Llamar a la función, la cual le regresará una lista con los datos de la diagonal de la matriz y mostrar la lista. En caso de que la matriz no sea una matriz cuadrada, deberá de mostrar el mensaje "la matriz no es cuadrada", esta verificación se debe hacer al leer la cantidad de renglones y columnas, de modo que si la matriz no es cuadrada el programa ya no continúa. Observa los ejemplos.

Entrada: <br>
Número de renglones de la matriz
Número de columnas de la matriz
Los datos de la matriz

Salida: <br>
Una lista que contiene los datos de la diagonal principal de la matriz

Ejemplos de ejecución del programa:
```
>>>3        <--- cantidad de renglones
>>>4        <--- cantidad de columnas
La matriz no es cuadrada      <-- Observa que si la matriz no es cuadrada no lee los datos de la matriz

>>>3        <--- cantidad de renglones
>>>3        <--- cantidad de columnas
>>>1        <--- datos de la matriz
>>>2
>>>3
>>>4
>>>5
>>>6
>>>7
>>>8
>>>9
[1, 5, 9]
```
-------------------------------------------------
# 12 Matrices: Menores a Número

Escribe una función que reciba una matriz como parámetro y regrese una lista con los números menores a 10 que se encuentran en la matriz. Se debe tener una función auxiliar que solicite los datos por teclado (número de renglones, número de columnas y elementos de la matriz) y genere la matriz correspondiente (lista con sublistas).
<b>Utiliza el archivo que ya viene incluido en tu entorno.</b><br><br>

Entrada:<br> 
Número de renglones (número entero)<br>
Número de columnas (número entero)<br>
Valores de la matriz (números enteros)<br>
(Se ingresa un valor por renglón y estrictamente en el orden citado).

Salida: <br>
Una lista con los números menores a 10.

Ejemplo de ejecución del programa.<br>
```
>>> 2
>>> 3
>>> 1 
>>> 25 
>>> 8
>>> 30
>>> 2
>>> 4
[1, 8, 2, 4]

>>> 2
>>> 0
[]
```
-------------------------------------------------
# 13 Centro de la matriz
Escribe una función centro_matriz que pregunta el número de renglones y número de columnas de una matriz, después pregunta cada valor entero de la matriz y regresa el centro de la matriz quitando el primer renglón, primera columna, último renglón y última columna.<br><br>

Entrada<br>
Dos números enteros que son el número de renglones y el número de columnas (en ese orden).
Los números enteros que son elementos de la matriz.
(Cada valor en un renglón y estrictamente en el orden citado).

Salida<br>
La matriz que corresponde al centro de la matriz (es decir la matriz original sin el primer y último renglón y sin la primera y última columna).

Ejemplos de ejecución del programa.<br>
```
>>> 1
>>> 1
>>> 1
[ ]

>>> 3
>>> 3
>>> 1
>>> 1
>>> 1
>>> 2
>>> 2
>>> 2
>>> 3
>>> 3
>>> 3
[ [2] ]

>>> 0
>>> 3
[ ]
```
-------------------------------------------------
# 14 Suma de matrices 
Desarrolla una función en Python que reciba dos matrices de números enteros y calcule su suma.
La suma de matrices toma dos matrices del mismo tamaño y regresa una matriz que contiene la suma los elementos que se encuentran en la misma posición:
Ejemplo:
 [ [ 2,   2], + [ [5,  8],  = [ [7, 10],
...[5,    4]].....[4, 10]]......[9, 14]]

En caso de que las matrices no sean del mismo tamaño se deberá mostrar el mensaje "Las matrices no son del mismo tamaño". 
Nota: Se debe incluir una función auxiliar que pida por teclado los valores de la matriz renglón por renglón, y genere la matriz correspondiente.

Entradas 
Números enteros separando los valores por espacios y que representan un renglón de la matriz.
Se sugiere utilizar la función <b>split</b> para generar una lista a partir de los datos dados en cada renglón. Para indicar el fin de la matriz ya no se teclea ningún número solo se presiona <b>enter</b>

Salida
La matriz resultante al sumar las dos matrices recibidas como entrada, o  el mensaje "Las matrices no son del mismo tamaño"

Ejemplos de ejecución del programa:
```
>>> 1 2
>>> 3 4
>>>  <------------------ enter sin teclear nada
>>> 5 6
>>> 6 1
>>>  <------------------ enter sin teclear nada
[ [6, 8], [9, 5] ]

>>> 1 2 1
>>>  <------------------ enter sin teclear nada
>>> 1 2
>>>  <------------------ enter sin teclear nada
```
Las matrices no son del mismo tamaño

-------------------------------------------------
# 15 Cambia Renglones
Escribe un programa que lee el número de renglones y de columnas de una matriz, después lee cada valor entero de la matriz, posteriormente pregunta el número del primer renglón y del segundo renglón a intercambiar y finalmente muestra la matriz con los renglones intercambiados.

Entrada
Número de renglones y el número de columnas de una matriz.
Los números enteros que son elementos de la matriz.
Dos números enteros que son el primer y segundo renglón que va a intercambiar.

Salida
Matriz con los renglones intercambiados.

Ejemplo de ejecución del programa:
```
>>>2   <--- número de renglones de la matriz
>>>3   <--- número de columnas de la matriz
>>>1   <--- datos de la matriz
>>>1
>>>1
>>>2
>>>2
>>>2
>>>1   <--- primer renglón a intercambiar. Observa que se usa el número 1 para el primer renglón.
>>>2   <--- segundo renglón a intercambiar. Observa que se usa el número 2 para el segundo renglón.
[[2, 2, 2],[1, 1, 1]]
```

Otro ejemplo
```
>>>3
>>>3
>>>1
>>>1
>>>1
>>>2
>>>2
>>>2
>>>3
>>>3
>>>3
>>>2
>>>3
[[1, 1, 1],[3, 3, 3],[2, 2, 2]]
```
