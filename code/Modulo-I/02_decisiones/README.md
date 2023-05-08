# Ejercicios de decisiones

# 01 IdentificaSigno
¿Positivo, negativo o cero?
Identifica si un número entero es positivo, negativo o cero.

El programa despliega un mensaje "Es positivo" "Es negativo" ó "Es cero" dependiendo de la entrada del usuario.

**Entradas:**
Un número entero

**Salida**
Un mensaje

Ejemplo:
```
Dame un número: -8
Es negativo

```

Ejemplo 2:
```
Dame un número: 0
Es cero

```
-------------------------------------------------
# 02 Licencia
Una persona puede obtener su licencia de manejo si es mayor de edad y tiene identificación oficial.

Escribe un programa en Python que lea la edad de una persona y si tiene (s/n) identificación oficial.

De salida debe mostrar Si  puede obtener su licencia o No la puede obtener.

**Entradas**
El programa va a preguntar por:
- la edad de la persona, debe ser un entero positivo.
- si tiene identificación o no. Debe ser un string, que contenga las letras "s" o "n"

**Salidas**
Añade el código necesario para que el programa imprima:
- **Trámite de licencia concedido** si la edad es mayor o igual a 18 y tiene identificación oficial
- **No cumples requisitos** si no cumple con los requisitos para la licencia
- Si la edad es negativa o el usuario ingresó cualquier otro caracter que no sea s o n cuando pides la identificación, debe mostrar el mensaje **Respuesta incorrecta**

La salida del programa debe de ser exactamente de la siguiente forma:

## Ejemplos
Ejemplo 1

```plaintext
Ingresa tu edad: 19
¿Tienes identificación oficial? (s/n): s
Trámite de licencia concedido
```
Ejemplo 2

```plaintext
Ingresa tu edad: 19
¿Tienes identificación oficial? (s/n): n
No cumples requisitos
```

Ejemplo 3
```plaintext
Ingresa tu edad: 12
No cumples requisitos
```

Ejemplo 4
```plaintext
Ingresa tu edad: 20
¿Tienes identificación oficial? (s/n): g
Respuesta incorrecta
```

-------------------------------------------------
# 03 Tipo de Triángulo
## Definición del problema  
Realiza un programa que sea útil para determinar si los números enteros X, Y y Z, proporcionados por el usuario, son medidas correctas para los lados de un triángulo y si lo son, debe decir si se trata de un triángulo Equilátero, Isósceles o Escaleno.

**NOTA:** X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:
Todos los números son mayores que cero
  * X + Y > Z   
  * X + Z > Y   
  * Y + Z > X  

es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.

El triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y el escaleno tiene los 3 lados diferentes.

**Entradas**  
El programa va a preguntar por tres **números enteros** uno en cada renglón.

**Salidas**  
Alguna de las siguientes palabras, según sea el tipo de triángulo para los valores dados: 
  * ES UN TRIANGULO EQUILATERO
  * ES UN TRIANGULO ISOSCELES  
  * ES UN TRIANGULO ESCALENO   
 
O bien, la frase: NO ES TRIANGULO si los valores introducidos por el usuario no corresponden a los lados de un triángulo, es decir no cumplen con alguna de las condiciones mencionadas arriba.

Escribe solamente uno de los 4 mensajes permitidos usando letras mayúsculas, no les pongas acentos en esta ocasión, escribe el mensaje exactamente como se describe.

## Ejemplos    
Ejemplo 1

```plaintext
Ingresa la medida del lado 1: 3
Ingresa la medida del lado 2: 3
Ingresa la medida del lado 3: 3
ES UN TRIANGULO EQUILATERO
```
Ejemplo 2

```plaintext
Ingresa la medida del lado 1: 4
Ingresa la medida del lado 2: 5
Ingresa la medida del lado 3: 6
ES UN TRIANGULO ESCALENO
```

Ejemplo 3
```plaintext
Ingresa la medida del lado 1: 3
Ingresa la medida del lado 2: 2
Ingresa la medida del lado 3: 3
ES UN TRIANGULO ISOSCELES
```

Ejemplo 4
```plaintext
Ingresa la medida del lado 1: 12
Ingresa la medida del lado 2: 3
Ingresa la medida del lado 3: 23
NO ES TRIANGULO
```
-------------------------------------------------
# 04 El mayor de 3 números
## Definición del problema  

Realiza un programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.

**NOTA:** NO puedes utilizar la función incorporada de Python: max(), debes hacerlo con condicionales.

**Entradas**  
El programa va a preguntar por tres **números enteros** uno en cada renglón.

**Salidas**  
El mayor de los tres números dados por el usuario.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 8
Ingresa el tercer número: -3
8
```
Ejemplo 2

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 1
Ingresa el tercer número: 12
12
```

-------------------------------------------------
# 05 Ordena 3 números
## Definición del problema  

Realiza un programa que ordena en forma ascendente tres números enteros x, y, z.

**NOTA:** NO puedes utilizar la función incorporada de Python: sort(), debes hacerlo con condicionales.

**Entradas**  
El programa va a preguntar por tres **números enteros** uno en cada renglón.

**Salidas**  
Los números de menor a mayor uno por renglón.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 8
Ingresa el tercer número: -3
-3
5
8
```
Ejemplo 2

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 1
Ingresa el tercer número: 12
1
5
12
```

-------------------------------------------------
# 06 Índice de masa corporal
## Definición del problema  

Escribe un programa que calcule el **IMC** (Índice de Masa Corporal) de una persona, el cual se utiliza para determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la siguiente fórmula:

indice = peso / altura^2

Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se clasifican los diferentes rangos de índice:

| Rango de índice |  Descripción  |  
| :-------------: |:-------------:| 
|índice < 20      | PESO BAJO     |
|20 <= índice < 25| NORMAL        |
|25 <= índice < 30| SOBREPESO     |
|30 <= índice < 40| OBESIDAD      |
|índice >= 40     | OBESIDAD MORBIDA|

**Entradas**  
Dos números **flotantes** (peso y altura) uno en cada renglón y recibidos en este orden.  

**Salidas**  
Un **string** correspondiente a la descripción del índice de masa corporal, tal como se ve en la tabla, todo en mayúsculas.  
Debes de verificar que tanto el peso como la altura sean mayores a 0, en caso de que alguno sea 0 o menor, se debe mandar el siguiente mensaje de error: *Revisa tus datos, alguno de ellos es erróneo*.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Peso en kg: 53
Altura en m: 1.66
PESO BAJO
```
Ejemplo 2

```plaintext
Peso en kg: 65
Altura en m: 0
Revisa tus datos, alguno de ellos es erróneo.
```

-------------------------------------------------
# 07 Día siguiente - considera año Bisiesto
## Definición del problema  

Escribe un programa que dada una fecha (año, mes y día), devuelva la fecha del día siguiente. Te recomiendo que antes de ponerte de codificar, verifiques todas las posibilidades que se pueden presentar.

Este problema debe considerar la verificación de año bisiesto. Recuerda que el siguiente algoritmo se puede usar para determinar si un año determinado es bisiesto:  
  * Los años bisiestos son cualquier año que es divisible por 4 (como 2012, 2016, etc).
  * Excepto si puede dividirse por 100, entonces no lo es (como 2100, 2200, etc).
  * A menos que pueda ser divisible por 400, como 2000, 2400.

Para este ejercicio, no validaremos las entradas, confiaremos que el usuario ingresará una fecha válida.

**Entradas**  
Año, día y mes (**enteros positivos**) en ese orden.

**Salidas**  
Año, día y mes (**enteros positivos**) en ese orden que corresponde al día siguiente ingresado como entrada.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Año: 2015
Mes: 2
Día: 13
2015
2
14
```

Ejemplo 2

```plaintext
Año: 2016
Mes: 2
Día: 28
2016
2
29
```

Ejemplo 3

```plaintext
Año: 2016
Mes: 12
Día: 31
2017
1
1
```

-------------------------------------------------
# 08 Punto con respecto a la circunferencia
Escriba un programa que pida el radio y las coordenadas del centro de una circunferencia, así como las coordenadas de un punto. El programa deberá indicar si el punto está sobre la circunferencia, dentro o fuera de ella. Investiga o recuerda la fórmula del calculo de distancia entre dos puntos porque la vas a necesitar.

**Entradas**
- radio (flotante)
- x1 Coordenada x del centro de la circunferencia (flotante)
- y1 Coordenada y del centro de la circunferencia (flotante)
- x2 Coordenada x del punto (flotante)
- y2 Coordenada y del punto (flotante)
- NOTA: Los datos deberán ser ingresados estrictamente en este orden.

**Salida**
- Un string que representa la posición del punto con respecto a la circunferencia: `"DENTRO"`, `"FUERA"`, `"SOBRE"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 6
FUERA

Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 5
SOBRE

Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 3
DENTRO
```

-------------------------------------------------
# 09 De Centímetros a Kilómetros, Metros y Centímetros

Escribe un programa que pida una distancia en centímetros y que escriba esa distancia en su equivalente en kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).

**Entrada**
- Un número entero que representa la distancia en centímetros.

**Salidas**
- El número de km, m y cm equivalente a la cantidad de centímetros dada por el usuario.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce los cm: 100
1 m

Introduce los cm: 240005
2 km
400 m
5 cm

Introduce los cm: 67
67 cm

Introduce los cm: 300004
3 km
4 cm

Introduce los cm: 1200500
12 km
5 m
```
El resultado se debe mostrar como se indica con cada valor en un renglón por separado, indicando las unidades correspondientes (km, m y cm en minúscula) y en el orden indicado. Si no hay valor para alguna de las tres unidades, no debe mostrar dicho renglón.

-------------------------------------------------
# 10 Cuadrante 
Escribe un programa que lea un número entero que se encuentre entre 0 y 360 que representa los grados del plano cartesiano y que muestre como resultado el número de cuadrante en donde se encuentra. 
En caso de que el grado caiga en un eje, tu programa debe mostrar la palabra `"eje"`.
En caso de que el grado sea menor a cero o mayor a 360,  tu programa debe mostrar la palabra `"excede"`.

**Entrada**
- Un número entero que representa una cantidad de grados.

**Salida**
- La palabra cuadrante (en minúsculas) seguida del número de cuadrante correspondiente (por ejemplo: `cuadrante 2`), o bien alguna de las palabras `eje` o `excede`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce los grados: -10
excede

Introduce los grados: 90
eje

Introduce los grados: 45
cuadrante 1

Introduce los grados: 215
cuadrante 3
```

-------------------------------------------------
# 11 Cuadrática
Realiza un programa para calcular los valores de la ecuación cuadrática `ax^2+bx+c` usando la fórmula cuadrática.
El programa debe leer tres valores enteros a, b y c, y encontrar los valores de x, considerando las siguientes restricciones:
- Si a = 0 y b = 0 se debe desplegar el mensaje `"No tiene solucion”`.
- Si a = 0 y b != 0 se debe despejar el valor de x = –c/b y mostrar este valor.
- Si a != 0 y b != 0 se debe calcular el discriminante.
      * Si el valor del discriminante es negativo debe mostrar el mensaje `"Raices complejas"`.
      * Si el valor del discriminante es positivo debe calcular y mostrar los dos valores de x, una en cada renglón.
      * En caso de que el discriminante sea cero se debe mostrar sólo un valor de x = -b/(2a).

**Entradas**
- Los tres valores enteros a, b, c uno en cada renglón y en ese orden.

**Salidas**
- El valor de la o las raices (si es el caso) uno en cada renglón, o alguno de los mensajes `"No tiene solucion"` o `"Raices complejas"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Da el valor de a: 1
Da el valor de b: 2
Da el valor de c: 3
Raices complejas

Da el valor de a: 0
Da el valor de b: 1
Da el valor de c: 2
-2.0

Da el valor de a: 1
Da el valor de b: 5
Da el valor de c: 6
-2.0
-3.0

Da el valor de a: 0
Da el valor de b: 0
Da el valor de c: 2
No tiene solucion

NOTA: Para mostrar la salida solamente muestra las variables en las que tienes el 
resultado de los cálculos, no le apliques ningún formato.
```


-------------------------------------------------
# 12 Minijuego Piedra, Papel o Tijera
Escriba un programa que simule el juego <a href="https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera">Piedra, papel, tijera</a> para dos jugadores (Ana y Juan).

Las reglas del juego son las siguientes:
- Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
- Piedra: se muestra el puño cerrado y se representa con un caracter `a`.
- Papel: se muestra la palma de la mano y se representa con un caracter `p`.
- Tijera: se muestra la palma de la mano con los dedos separados en dos grupos y se representa con un caracter `t`.
- El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
- El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
- El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
- Caso de empate cuando dos jugadores elijan el mismo elemento.

**Entradas**
- Dos caracteres (a, p o t), cada uno en un renglón y representan la tirada de Ana y Juan, en ese orden.

**Salida**
- Mensaje de quien es el ganador en el siguiente formato: `"Gana Ana"` o `"Gana Juan"` o `"Empate"`. 
- En el caso de que ingresen algún string de más de un caracter se debe desplegar el siguiente mensaje `"Las tiradas deben ser un caracter"`, si son de un sólo caracter pero alguna de ellas no corresponde a un caracter válido, el mensaje a desplegar es `"Tirada incorrecta"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Tirada de Ana: a
Tirada de Juan: p
Gana Juan

Tirada de Ana: t
Tirada de Juan: p
Gana Ana

Tirada de Ana: a
Tirada de Juan: a
Empate

Tirada de Ana: piedra
Tirada de Juan: a
Las tiradas deben ser un caracter

Tirada de Ana: p
Tirada de Juan: r
Tirada incorrecta
```

-------------------------------------------------
# 13 Pass Fail Grade
El programa va a preguntar por una calificación numerica, entre 0 y 100.
Añade el código necesario para que el programa imprima **Pass** si la
calificación es mayor o igual a 70, o que imprima **Fail** si la
calificación es menor a 70.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter grade: 90
Pass
```

Únicamente necesitas modificar la función **check_grade** y asegurarte de
que regrese la palabra correcta.

-------------------------------------------------
# Número más grande
El programa va a preguntar por tres números, y al final debe imprimir sólo
el número que es mayor que los demás.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter first number: 6
Enter second number: 9
Enter third number: 4
9
```

```plaintext
Enter first number: 4
Enter second number: 3
Enter third number: 1
4
```

Únicamente necesitas modificar la función **largest_of_three**. <br>
Elimina la palabra __pass__ y escribe el código necesario.<br>
Asegurarte de que la función regrese el valor correcto.

-------------------------------------------------
# 15 Tarifa de estacionamiento
Un estacionamiento público cobra una tarifa que varía según el tiempo que un
auto haya permanecido dentro. La tarifa se determina según lo siguiente:<br>
* 2 horas por $5.00
* $12.00 Tercera hora o fracción
* A partir de la 4ta hora se cobra fracción 
* $100.00 Boleto pedido
* Fracciones: 
    * 1  - 15 mins: $5.00
    * 16 - 30 mins: $3.00
    * 31 - 45 mins: $2.00
    * 46 - 60 mins: $2.00

El programa va a preguntar por dos números, la cantidad de horas, y la cantidad
de minutos que duró un carro en el estacionamiento.
Calcula el precio que debe pagar un auto que haya permanecido ese tiempo.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter number of hours: 1
Enter number of minutes: 40
Total to pay: 5
```

```plaintext
Enter number of hours: 3
Enter number of minutes: 1
Total to pay: 22
```

```plaintext
Enter number of hours: 6
Enter number of minutes: 50
Total to pay: 65
```

-------------------------------------------------
# 16 Cuadrante en el plano cartesiano 
El plano cartesiano se divide en 4 cuadrantes, que van en sentido contrario
a las manecillas del reloj. El cuadrante depende del signo de las coordenadas
del punto en X y Y.

El programa va a preguntar por dos números, las coordenadas en X y en Y,
y luego imprimirá en qué cuadrante se encuentra el punto dado.
Las respuestas pueden incluir, además de los cuatro cuadrantes
(I, II, III y IV), el **Origin** o los puntos sobre los ejes: **X axis** o
**Y axis**.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter X coordinate of the point: 0
Enter Y coordinate of the point: 0
The point is in quadrant: Origin
```

```plaintext
Enter X coordinate of the point: 2
Enter Y coordinate of the point: 2
The point is in quadrant: I
```

```plaintext
Enter X coordinate of the point: -4.7
Enter Y coordinate of the point: 0
The point is in quadrant: Y axis
```

-------------------------------------------------
# 17 Next day
Los meses del año tienen diferente número de días, y en particular el mes de
Febrero varía en sus días según los años bisiestos. Por lo tanto hay varias
decisiones involucradas al solicitar el día siguiente a una fecha.

Cómo referencia, los meses de enero, marzo, mayo, julio, agosto, octubre y
diciembre tienen 31 días. Mientras que abril, junio, septiembre y noviembre
tienen 30 días. Febrero puede tener 28 o 29, según el año.

Los años bisiestos son aquellos que son divisibles entre 4, pero hay algunos
[casos especiales](https://www.timeanddate.com/date/leapyear.html#rules).
Los años que son divisibles entre 100 **no** son bisiestos, a menos que sean
divisibles entre 400.

El programa va a preguntar por tres números, el día, mes y año actual,
y debe imprimir la fecha del día siguiente.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter the day: 28
Enter the month: 2
Enter the year: 2020
Next day: 29/2/2020
```

```plaintext
Enter the day: 31
Enter the month: 12
Enter the year: 2021
Next day: 1/1/2022
```

-------------------------------------------------
# 18 Año Bisiesto
El siguiente algoritmo se puede usar para determinar si un año determinado es bisiesto:

   * Los años bisiestos son cualquier año que es divisible por 4 (como 2012, 2016, etc).  
   * Excepto si puede dividirse por 100, entonces no lo es (como 2100, 2200, etc).  
   * A menos que pueda ser divisible por 400, como 2000, 2400.

Escribe el programa que determine si un año es bisiesto o no (**True o False**)

**Entradas**  
Un año (**valor entero mayor a cero**).
  
**Salidas**  
La salida será un valor **True** para indicar que el año es bisiesto y **False** si no lo es.   
Si el dato es 0 o menor, deberá mostrar el siguiente mensaje: **Dato incorrecto**
 
## Ejemplos  

Ejemplo 1    

```plaintext
Año: 2012
True
```

Ejemplo 2

```plaintext
Año: 2100
False
```

Ejemplo 3

```plaintext
Año: 1995
False
```

Ejemplo 4

```plaintext
Año: 0
Dato incorrecto
```
