# Ejercicios de funciones

# 01 Convertidor a centímetros 
Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir tres funciones:
- La función **pies_cm(pies)** que recibe una cantidad en `pies`(entero positivo) y devuelva su equivalencia en centímetros.
- La función **pulgadas_cm(pulgadas)** que recibe una cantidad en `pulgadas`(entero positivo) y devuelva su equivalencia en centímetros.
- La función **yardas_cm(yardas)** que recibe una cantidad en `yardas`(entero positivo) y devuelva su equivalencia en centímetros.

**Entradas**
- La opción a ejecutar (`1. pies a cm, 2. pulgadas a cm, 3. yardas a cm`). 
- Un valor entero positivo que corresponde a la cantidad en la medida de acuerdo con la opción tecleada (sólo el número).

**Salida**
- La cantidad equivalente en centímetros (sólo el número). 
- En caso de que el número de opción sea diferente a 1, 2, o 3 se desplegará el mensaje: `Error`.
- En caso de que el valor a convertir sea 0 o menor se desplegará el mensaje: `Error`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: 1
Introduce la cantidad: 1
30.48

1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: 2
Introduce la cantidad: 1
2.54

1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: -5
Introduce la cantidad: 1
Error
```

-------------------------------------------------
# 02 Calcula Grado
Escribe un programa en el cual definas la función calcula_grado(numero). Esta función debe recibir un número flotante entre 0 y 1, y debe regresar una nota alfabética de acuerdo a la siguiente tabla.
<table>
    <tr>
        <td>Score</td>
        <td>nota</td>
    </tr>
    <tr>
        <td>mayor a 0.9</td>
        <td>A</td>
    </tr>
    <tr>
        <td>mayor a 0.8</td>
        <td>B</td>
    </tr>
    <tr>
        <td>mayor a 0.7</td>
        <td>C</td>
    </tr>
    <tr>
        <td>mayor a 0.6</td>
        <td>D</td>
    </tr>
    <tr>
        <td>otro dentro del rango</td>
        <td>F</td>
    </tr>
</table>

*Cualquier otro valor fuera del rango debe regresar "score incorrecto"*

```
Entrada
Un número flotante entre 0 y 1.

Salida
La letra correspondiente al score asignado de acuerdo a la tabla de arriba.
Si la entrada no está dentro del rango de 0 a 1 (inclusive), la función debe regresar la leyenda "score incorrecto"
La función main( ) debe llamar a la función calcula_grado(valor) y debe desplegar el valor que retorna la función.

La salida del programa debe de ser exactamente de la siguiente forma:

Ingresa Un valor entre 0.0 y 1.0: 0.98
A                                                              
Ingresa Un valor entre 0.0 y 1.0: -5.1
score incorrecto
Ingresa Un valor entre 0.0 y 1.0: 0.8
C  
Ingresa Un valor entre 0.0 y 1.0: 0.65
D
Ingresa Un valor entre 0.0 y 1.0: 50
score incorrecto
```

-------------------------------------------------
# 03 Tienda de Sillas
En una tienda de sillas para oficina se venden de 3 tipos: básica, estándar y de lujo.
Además existen los clientes normales y los clientes frecuentes.

El precio de las sillas es:
- Básica $700.00 c/u
- Estándar $900.00 c/u
- De Lujo $1,500.00 c/u

El dueño de la tienda ha decidido dar un descuento del 20% a los <b>clientes frecuentes</b>

Además ha decidido aplicar la siguiente política de descuentos por mayoreo a los
<b> clientes normales </b>:
- si su compra es >= $10,000 y < $20,000 un 10% de descuento
- si su compra es >= $20,000 un 15% de descuento

Escribe un programa que lea el tipo de silla (que es una letra mayúscula que puede ser B, E, L),
el tipo de cliente (que es una letra mayúscula que puede ser F o N) y
la cantidad a comprar (que es un número entero).  Supón que solo se va a comprar de un tipo de silla.

####  El programa debe tener las siguientes funciones:
- Función llamada  total_antes_descuento que recibe como parámetros: tipo_silla y la cantidad:
La función retorna el total incial, antes del descuento.
- Función llamada calcula_descuento que recibe como parámetros: el total inicial y el tipo_cliente:
La función retorna el monto del descuento.

El programa debe calcular y mostrar los siguientes datos (todos los datos son flotantes y debes mostrar uno en cada renglón):
- El total inicial, antes de aplicar descuento
- La cantidad de dinero que se otorga por descuento y
- El total a pagar por el cliente.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Tipo silla: L
Tipo cliente: F
Cantidad de sillas: 10
Total sin dcto.  $15000.0
Descuento        $ 3000.0
Total a pagar    $12000.0


Tipo silla: L
Tipo cliente: N
Cantidad de sillas: 10
Total sin dcto.  $15000.0
Descuento        $ 1500.0
Total a pagar    $13500.0


Tipo silla: E
Tipo cliente: N
Cantidad de sillas: 10
Total sin dcto.  $ 9000.0
Descuento        $    0.0
Total a pagar    $ 9000.0


Tipo silla: B
Tipo cliente: N
Cantidad de sillas: 30
Total sin dcto.  $21000.0
Descuento        $ 3150.0
Total a pagar    $17850.0

```

-------------------------------------------------
# 04 Convierte binario a decimal
Diseña un programa que incluya la función binario_decimal que convierta números binarios (base 2)
en números decimales (base 10).
La función deberá recibir un string que contenga el número binario a convertir y
regresar un número entero equivalente en base 10.
Si el string recibido es de tamaño 0 o no está formada por sólo 1s y 0s se devuelve un -1.

Escribe después la función main que lea el string,
lo envíe a la función y luego muestre el valor de retorno de la función en la pantalla.

#### Entrada
Un string formado por 1s y 0s.

#### Salida
Un número entero que representa la conversión del binario al formato decimal.
Si el string recibido es de tamaño 0 o no está formada por sólo 1s y 0s se devuelve un -1.

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente
con el formato y/o tipo de dato que se te pide como salida.

La salida del programa debe de ser exactamente de la siguiente forma:

```
1111111
127

Hola
 -1

0a
-1

1010
15

```

-------------------------------------------------
# 05 Área total de un prisma rectangular
Realiza una **función** que obtenga el área de un rectángulo. La función debe recibir dos parámetros (números decimales) que representan la base y la altura del rectángulo y debe regresar el área calculada (número decimal).

Realiza una segunda **función** que obtenga el área total de un prisma rectangular con base rectangular. El área total de un prisma de este tipo es igual a la suma de las áreas de cada una de sus caras. *Utiliza llamadas a la función anterior para este cálculo*.

Manda a llamar a esta última función en el main con datos del usuario. 

Ejemplo de ejecución

```
Dame la base: 21.3
Dame la altura: 10
Dame la profundidad: 2.0
El área total del prisma es: 551.2
```

-------------------------------------------------
# 06 Volumen de un prisma rectangular
Realiza una **función** que obtenga el área de un rectángulo. La función debe recibir dos parámetros (números decimales) que representan la base y la altura del rectángulo y debe regresar el área calculada (número decimal).

Realiza una segunda **función** que obtenga el volumen de un prisma rectangular con base rectangular. El volumen de un prisma de este tipo es igual al área de la base por la altura de la figura. *Utiliza llamadas a la función anterior para este cálculo*.

Manda a llamar a esta última función en el main con datos del usuario. 

Ejemplo de ejecución

```
Dame la base: 21.3
Dame la altura: 10
Dame la profundidad: 2.0
El volumen del prisma es: 426.0
```

-------------------------------------------------
# 07 Tarjetería Española
Un pliego de papel albanene sirve para realizar 12 tarjetas en tarjetería española. Además, un plumón para tarjetería española sirve para hacer 35 tarjetas. Realiza un programa que utilice una **función** y que indique cuántas tarjetas de tarjetería española se pueden hacer *máximo* dada una cantidad de pliegos de papel albanene (número entero) y de plumones (número entero).

Manda a llamar a esta función en el main con datos del usuario. 

Ejemplo de ejecución

```
Dame la cantidad de pliegos de papel albanene: 7
Dame la cantidad de plumones: 2
El número máximo de tarjetas que se pueden hacer es: 70
```


-------------------------------------------------
# 08 Área de un rectángulo
Realiza una **función** que obtenga el área de un rectángulo. Mándala a llamar en el main con datos del usuario. La función debe recibir dos parámetros (números decimales) que representan la base y la altura del rectángulo y debe regresar el área calculada (número decimal).

Ejemplo de ejecución

```
Dame la base: 21.3
Dame la altura: 10
El área del rectángulo es: 213.0
```

-------------------------------------------------
# 09 Oraciones
Realiza una **función** que reciba una cadena de caracteres y que indique cuántas oraciones terminadas por un punto hay. Utiliza un ciclo para practicar el tema.

Manda a llamar a esta función en el main con datos del usuario. 

Ejemplo de ejecución

```
Dame un párrafo: Hola. Buenos días.
Número de oraciones terminadas por un punto: 2
```

