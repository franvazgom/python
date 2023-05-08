# Ejercicios de ciclos

# 01 Cuenta números

Agrega una nueva línea abajo del comentario con el código para que lea un número positivo n,
e imprima todos los números en orden desde el 1 hasta n.
Cada uno de los números debe ser impreso en una linea por separado.

#### Entrada
Un número entero positivo n

#### Salida
Los números enteros desde 1 hasta n, uno en cada renglón

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

La salida del programa debe de ser exactamente de la siguiente forma:

```
5
1
2
3
4
5



15
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

10
1
2
3
4
5
6
7
8
9
10

```
-------------------------------------------------
# 02 Suma números
Escribe un programa que sume los números enteros (positivos y negativos) que el usuario teclee y se detenga hasta que el usuario teclee un cero.

#### Entrada
Una secuencia de números enteros positivos o negativos. La secuencia debe terminar con un 0.

#### Salida
La suma de los números tecleados.

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

El programa debe funcionar de la siguiente forma:

```
1
2
0
3

100
200
0
300

1
-1
0
0

1
2
3
0
6

```

-------------------------------------------------
# 03 Suma n números consecutivos
Escribe una función que reciba como parámetro un número entero positivo n, después debe calcular la suma 1+2+3+...+n. Finalmente regrese el resultado de la suma y en la función main imprime ese resultado a pantalla.

La salida del programa debe de ser solamente el valor de la suma. Observa el ejemplo.

**Entrada:**
Un número entero positivo n

**Salida:**
El resultado de la suma 1+2+3...+n

**Ejemplo de ejecución del programa:**
```
>>>6
21
```

-------------------------------------------------
# 04 Lista de Precios
## Descripción del programa  

Escribe un programa que lea la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos. El programa debe mostrar en la pantalla el precio correspondiente a cada artículo pedido, el programa debe repetirse mientras el usuario no teclee la clave X, cuando el usuario teclee la clave X el programa debe mostrar en la pantalla el total de la compra del cliente.

Clave | Precio
------|-------
  A   |  120
  B   |  250
  C   |  360


**Entrada**  
Una secuencia de letras que representan la clave del artículo que se va a comprar. Debe terminar con X que significa que ya se terminó de comprar.

**Salida**  
Para cada letra que se ingrese, se debe mostrar el precio del artículo correspondiente.
Después de que se teclee la letra X se debe mostrar el total de los artículos elegidos.

**Ejemplo de la ejecución del programa:**  
```
>>>B              
250               
>>>A                 
120               
>>>X                 
370 
```

-------------------------------------------------
# 05 Promedio Sencillo
## Descripción del programa

Escribe un programa que primero lea el valor n, que es la cantidad de números que se van a promediar. 
Después debe leer los n números positivos (flotantes), promediarlos y mostrar el promedio.

**Entrada**  
Un número entero n y después los n números flotantes

**Salida**  
El promedio de los n números leídos.

**Ejemplo de ejecución del programa:**  
```
>>>3                        
>>>2.5                   
>>>3.8                   
>>>4.6                  
3.633333333333333   
```

-------------------------------------------------
# 06 Promedio con Decisión 
## Descripción del programa  
Escribe un programa que calcule el promedio de una serie de números flotantes, no se sabe inicialmente la cantidad de valores a promediar, así que el programa debe seguir leyendo números hasta que el usuario teclee un número negativo. Ten cuidado de no considerar el número negativo dentro del promedio.

**Entrada**  
Una serie de números flotantes. La serie termina cuando se teclea un número negativo.

**Salida**  
El promedio de los números leídos.

**Ejemplo de ejecución del programa:** 
``` 
>>>2.5                   
>>>6.3                   
>>>4.7                  
>>>-2.1                     
4.5  
```

-------------------------------------------------
# 07 Cantidad de Pares
## Descripción del programa

Desarrolla un programa en Python que solicite números enteros hasta que el número ingresado sea un número negativo.
El programa deberá de mostrar cuántos números ingresados fueron pares.

**Entrada**  
Números enteros que reciben hasta que el número ingresado sea un número negativo.

**Salida**  
Cantidad de números pares que ingresó el usuario. El 0 cuéntalo como par. El formato para mostrar la salida es el texto: "Total de pares=" y seguido, sin espacio, el número de pares encontrados.

**Ejemplo de ejecución de un programa**  
```
>>> 4
>>> 3
>>> 11
>>> 42
>>> 0
>>> -2
Total de pares=3
```
(Son 3 números pares los ingresados, el 4, el 42 y el 0, el -2 es el negativo con el que terminamos el ciclo) 

-------------------------------------------------
# 08 Rango de Pares Simple
Escribe un programa que lea los valores enteros a y b y muestre todos los números pares que se encuentran desde a hasta b.
Supón que a < b.
Si a y/o b son pares, deben de ser incluidos.
El 0 es considerado par.

**Entrada**
Los números enteros positivos a y b. Uno en cada renglón.

**Salida**
La lista de números pares que están dentro de ese rango (incluyendo los límites). Mostrar un número en cada renglón.

**Ejemplos de ejecución del programa**
```
>>> 3
>>> 12
4
6
8
10
12
```

-------------------------------------------------
# 09 Alterna Caracteres
Escribe un programa que lea un valor `n` y que muestre en la pantalla `n` caracteres que alternan entre `#` y `%`.

Los caracteres se deben mostrar uno en cada renglón.

Observa que el primer caracter que se debe mostrar siempre es `#`

## Entrada

Un valor entero positivo `n`

## Salida
Una secuencia de caracteres que muestra el número de renglón y luego un caracter inicia con `#` y alterna entre `#` y `%`. 

La salida del programa debe de ser exactamente de la siguiente forma:

Ejemplo de ejecución del programa:

Entrada:
7

Salida:
```
1-#
2-%
3-#
4-%
5-#
6-%
7-#
```

-------------------------------------------------
# 10 Alterna Caracteres
Escribe un programa que lea un valor `n` y que muestre en la pantalla `n` caracteres que alternan entre `#` y `%`.

Los caracteres se deben mostrar uno en cada renglón.

Observa que el primer caracter que se debe mostrar siempre es `#`

## Entrada

Un valor entero positivo `n`

## Salida
Una secuencia de caracteres que inicia con `#` y alterna entre `#` y `%`. Un caracter en cada renglón.

La salida del programa debe de ser exactamente de la siguiente forma:

Ejemplo de ejecución del programa:

Entrada:
7

Salida:
```
#
%
#
%
#
%
#
```

-------------------------------------------------
# 11 Suma de dígitos
Escribe un programa que muestre la suma de los dígitos de un número entero, el número puede ser positivo o negativo, la suma siempre será positiva.
La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Escribe un numero entero: 2975
23
```

```
Escribe un numero entero: -517
13
```

-------------------------------------------------
# 12 Número al cuadrado mayor que N
Escribe un programa que reciba un número entero y como resultado, debe encontrar el menor número tal que al elevarlo al cuadrado sea mayor que el número N dado por el usuario.

tip:  Iniciar con una variable igual a 1, checar si la variable al cuadrado es mayor que N, si no lo es, entonces incrementar la variable y repetir.

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Escribe un numero : 30
6
```

(El resultado es 6 porque 6x6 es 36 y es el menor número que al elevarlo al cuadrado es mayor al número recibido que es el 30, por ejemplo 5 no nos serviría porque su cuadrado es 25 y no es mayor a 30)

-------------------------------------------------
# 13 Factorial de un número
Escribe un programa que calcule el factorial de un número N, donde N es solicitado al usuario.  
El factorial de un número es:  

Si N=0 o N=1, el factorial es 1  
Si N es cualquier número positivo se calcula como  
 N! = 1 * 2 * 3 * ... * N.  

Por ejemplo factorial de 4 es 1 * 2 * 3 * 4 = 24

Si el usuario ingresa un valor negativo se debe mostrar el siguiente mensaje:  
"Factorial no definido para negativos"

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Escribe un numero entero no negativo para calcular su factorial: 4
24
```

```
Escribe un numero entero no negativo para calcular su factorial: -2
Factorial no definido para negativos
```

```
Escribe un numero entero no negativo para calcular su factorial: 3
6
```

-------------------------------------------------
# 14 Pares dentro de un rango
Escribe un programa que contenga una función en Python que reciba dos números enteros positivos diferentes a cero que representan los límites de un rango y despliegue los números pares que se encuentran en el rango de menor a mayor (se incluyen los dos límites)

Si no hay pares en el rango dado, se manda el mensaje "No hay pares"

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Valor 1: 4
Valor 2: 9
4
6
8
```

```
Valor 1: 3
Valor 2: 3
No hay pares
```

```
Valor 1: 9
Valor 2: 2
2
4
6
8
```

-------------------------------------------------
# 15 Números primos
Escribe un programa que reciba un entero y devuelva True si es un número primo y False si NO es un número primo.  
Para este ejercicio, vamos a asumir que los numeros primos inician en 2.

La salida del programa debe de ser solamente un True o un False de la siguiente forma:

```
Escribe un numero entero : 1
False
```

```
Escribe un numero entero : -3
False
```

```
Escribe un numero entero : 5
True
```

-------------------------------------------------
# 16 Cálculo de intereses
En una cuenta de inversión tengo una cantidad X de dinero, el banco ofrece un rendimiento de un porcentaje de interés anual, donde cada mes el porcentaje de interés calculado se acumula al saldo de la cuenta, es decir, cada mes el saldo de la cuenta al final del mes, es igual a el saldo en ese momento más el cálculo del interés mensual.

Por ejemplo, si tienes 1000 pesos al inicio del año y el banco te da un porcentaje de rendimiento del 12% anual (es decir 1% mensual), al final de enero lo que tengo es 1010 pesos. En febrero, calculo el interés mensual pero partiendo de esos 1010 por lo que al final de febrero tendré 1020.10 y así sucesivamente cada mes.

Utiliza un ciclo for para calcular cuánto dinero voy a tener al final del año en la cuenta.   
Recuerda que el interés que se pide es anual, pero se genera mes con mes.

Si alguno de los datos, o los dos son negativos, se manda a pantalla el siguiente mensaje:
"Error en los datos"

La salida del programa debe de ser solamente la cantidad total al final del año, y como es dinero, debe ir con dos digitos después del punto decimal:

```
Escribe la cantidad de dinero inicial : 1000
Escribe el porcentaje de interes anual : 10
1104.71
```

```
Escribe la cantidad de dinero inicial : 1000
Escribe el porcentaje de interes anual : -10
Error en los datos
```

-------------------------------------------------
# 17 Invertir dígitos
El programa debe pedir un número entero al usuario, y después imprimir en
pantalla un número nuevo con los dígitos del primero en órden inverso.
El programa debe aceptar únicamente números de maximo 6 digitos. Para números
de más digitos, el programa debe imprimir `Too long`.

**Sugerencia**: Utiliza los operadores de division entera y módulo para
separar los dígitos.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 123
321
```

```
Enter a number: -8534
-4358
```

```
Enter a number: 12345678
Too long
```

-------------------------------------------------
# 18 Pino de navidad
Dibuja un pino de navidad en la pantalla <br>
El programa debe pedir un número entero **N** al usuario, que representa la altura
del pino.
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de asteriscos, de manera que se dibuje un pino.

**Nota 1**: Cuida el número de espacios y asteriscos a imprimir,
especialmente los espacios a la izquierda de los asteriscos.
No debe haber espacios a la derecha del último asterisco de cada linea.

**Nota 2**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y asteriscos correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero

## Salida

Varias lineas que contienen sólo espacios y asteriscos

Ejemplos:

```
Enter tree height: 0
```

```
Enter tree height: 3
  *
 * *
* * *
```

```
Enter tree height: 10
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
```

-------------------------------------------------
# 19 Pirámide de letras
El programa debe pedir un número entero **N** al usuario, que representa
la altura de la pirámide. El número debe ser entre 1 y 26
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de letras mayusculas. Iniciando siempre con la __A__ y avanzando
hasta donde permita el ancho de cada nivel.

**Nota 1**: Utiliza ciclos **for** para simplificar el código

**Nota 2**: Cuida el número de espacios y letras a imprimir,
especialmente los espacios a la izquierda de las letras.
No debe haber espacios a la derecha de la última letra de cada linea.

**Nota 3**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y letras correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero entre 1 y 26

## Salida

Si el número está fuera de rango, sólo imprimir el mensaje: `Out of range`.

De otra forma, imprimir varias lineas que contienen sólo espacios
y letras mayusculas, y que forman patrones como los mostrados a continuación.

Ejemplos:

```
Enter pyramid height: 0
Out of range
```

```
Enter pyramid height: 27
Out of range
```

```
Enter pyramid height: 3
    A
  A B A
A B C B A
```

```
Enter pyramid height: 5
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
```

```
Enter pyramid height: 20
                                      A
                                    A B A
                                  A B C B A
                                A B C D C B A
                              A B C D E D C B A
                            A B C D E F E D C B A
                          A B C D E F G F E D C B A
                        A B C D E F G H G F E D C B A
                      A B C D E F G H I H G F E D C B A
                    A B C D E F G H I J I H G F E D C B A
                  A B C D E F G H I J K J I H G F E D C B A
                A B C D E F G H I J K L K J I H G F E D C B A
              A B C D E F G H I J K L M L K J I H G F E D C B A
            A B C D E F G H I J K L M N M L K J I H G F E D C B A
          A B C D E F G H I J K L M N O N M L K J I H G F E D C B A
        A B C D E F G H I J K L M N O P O N M L K J I H G F E D C B A
      A B C D E F G H I J K L M N O P Q P O N M L K J I H G F E D C B A
    A B C D E F G H I J K L M N O P Q R Q P O N M L K J I H G F E D C B A
  A B C D E F G H I J K L M N O P Q R S R Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P Q R S T S R Q P O N M L K J I H G F E D C B A
```
-------------------------------------------------
# 20 Triángulo de asteriscos
El programa debe pedir un número entero **N** al usuario, que representa la altura
del triángulo.
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de asteriscos, de manera que se dibuje un triángulo con un ángulo
recto del lado derecho de la base.

**Nota 1**: Cuida el número de espacios y asteriscos a imprimir,
especialmente los espacios a la izquierda de los asteriscos.
No debe haber espacios a la derecha del último asterisco de cada linea.

**Nota 2**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y asteriscos correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero

## Salida

Varias lineas que contienen sólo espacios y asteriscos

Ejemplos:

```
Enter triangle height: 0
```

```
Enter triangle height: 3
  *
 **
***
```

```
Enter triangle height: 10
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
```

-------------------------------------------------
# 21 Conjetura Ulam
El programa debe pedir un número entero positivo mayor a 0 al usuario.
A partir de ese número, se va a generar una secuencia nueva, según la
Conjetura Ulam (también llamada Collatz o "hailstone sequence").
La secuencia comienza con el número dado por el usuario, y termina con el
número 1. Para llegar a ello, se toma el número inicial y se modifica según
las siguientes reglas:

- Si el número es par, se divide entre 2 (división entera)
- Si el número es impar, se multiplica por 3 y se le suma 1

El proceso sigue con el nuevo número, hasta que se obtenga el 1.

**Sugerencia**: Utiliza el operador de division entera para los números pares.

**Sugerencia**: Utiliza concatenación de strings (+) para construir un string
más grande que contenga toda la secuencia y poder imprimir sólo ese string.
Cuida que haya sólo un espacio entre cada número, y que no haya un espacio al
final

Si el número ingresado no es mayor a 0, el programa debe imprimir:
`Invalid input`

## Entrada

Un número entero positivo mayor a 0

## Salida

Un string con la secuencia correcta según las reglas.

Ejemplo de ejecución del programa:
```
>>> 6
6   --------------  es par, se divide por 2
3   -------------   es impar, se multiplica por 3 y se suma 1
10 --------------  es par, se divide por 2
5 ---------------	es impar, se multiplica por 3 y se suma 1
16 -------------   es par se divide entre 2
8   -------------   es par se divide entre 2
4   -------------   es par se divide entre 2
2   -------------   es par se divide entre 2
1
```
(La explicación de la operación a realizar es sólo para la comprensión del
problema, el programa sólo desplegará los números de la conjetura,
en un sólo renglón y separados por un espacio)

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 8
8 4 2 1
```

```
Enter a number: 3
3 10 5 16 8 4 2 1
```

```
Enter a number: 0
Invalid input
```

-------------------------------------------------
# 22 Multiplicación rusa
El programa debe pedir dos números enteros positivos, incluyendo 0.
Con estos números, llamados **factor1** y **factor2**, se realizan
las siguientes operaciones:

- El **factor1** se multiplica repetidamente por 2
- El **factor2** se divide repetidamente entre 2 (división entera),
    hasta que llegue a ser igual a 1

Para obtener la multiplicación, se suman todos los valores obtenidos de
**factor1** correspondientes a los valores impares de **factor2**.

El proceso a seguir de manera más gráfica es:
```
factor1: 5
factor2: 12
factor1----factor2---se suma ?
5           12	       no
10          6	       no
20          3	       si
40          1	       si
La multiplicación rusa es = 20 + 40  = 60
```

**Sugerencia**: Utiliza concatenación de strings (+) para construir un string
más grande que contenga toda la secuencia y poder imprimir sólo ese string.
Cuida que haya sólo un espacio entre cada número, y que no haya un espacio al
final

## Entrada

Dos números enteros positivos mayores o iguales a 0

## Salida

Una serie de renglones, donde cada renglón es un paso en el proceso, y
contiene los dos factores separados por un espacio.
Al final se debe imprimir otro renglón con el número resultante de la
multiplicación.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter factor 1: 3
Enter factor 0: 0
0
```

```
Enter factor 1: 0
Enter factor 2: 4
0 4
0 2
0 1
0
```

```
Enter factor 1: 37
Enter factor 0: 12
37 12
74 6
148 3
296 1
444
```

```
Enter factor 1: 12
Enter factor 0: 37
12 37
24 18
48 9
96 4
192 2
384 1
444
```

-------------------------------------------------
# 23 Números de Fibonacci
Calcular un número especifico en la secuencia de Fibonacci <br>

La secuencia de Fibonacci es una serie de números que inicia de la
siguiente forma:

```
0 1 1 2 3 5 8 13 21 34 55 ...
```

La característica que tiene es que cada número de la serie se calcula como
la suma de los dos números anteriores. De manera que el siguiente número sería
`34 + 55 = 89`.

Para efectos de este programa, asignaremos un número de posición (o índice) a
cada número de la secuencia, comenzando con el 0. Esto se puede visualizar
de la siguiente forma:

```
Serie:  0 1 1 2 3 5 8 13 21 34 55 ...
Indice: 0 1 2 3 4 5 6 7  8  9  10 ...
```

Escribe un programa que pida al usuario el índice, como un número entero
positivo. El programa debe calcular el número de Fibonacci correspondiente a
dicho ínidice. Por ejemplo, si el usuario da el número `9`, el programa debe
imprimir el número `34`.

**Nota**: Sólo necesitas recordar los dos números anteriores.
Debes empezar con los números `0` y `1`.
Debes utilizar un ciclo **while** para resolver este problema.

## Entrada

Un número entero positivo mayor o igual a 0

## Salida

Un número de la secuencia de Fibonacci.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 0
0
```

```
Enter a number: 3
2
```

```
Enter a number: 20
6765
```

