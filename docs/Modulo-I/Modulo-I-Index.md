<img src="../../images/LogoMagicPython.png" width="100">

# Python - Programación estructurada

# Tabla de contenido
1. [Introducción](#introduction)
2. [Objetivos](#objectives)
3. [Requerimientos de software](../References.md)
4. [Un vistazo al IDE y la consola](#terminal)
5. [Operadores aritméticos](#arithmetic_operators)
6. [Hola mundo en python](#hello_world)
7. [¿Qué sucede internamente cuando se ejecuta un programa](#what_happening)
8. [Comentarios](#comments)
9. [Variables y Tipos de datos](#data_type)
10. [input - keyboard](#input_keyboard) 
11. [Ejercicios - Básicos](#basic_exercise)
10. [String funciones](#string_functions)

## Introducción <a name="introduction"></a> 
Este es un módulo **básico de programación** donde puedes aprender a programar en el lenguaje python de manera estructurada. Si ya sabes programar en cualquier otro lenguaje, seguramente puedes avanzar mucho más rápido. Finalmente, si ya conoces el lenguaje python y solo estas reforzando tus habilidades de programación puedes intentar realizar los ejercicios propuestos en la carpeta `code/moduloI` 

## Objetivos <a name="objectives"></a>
El contenido de este curso pretende:  
* Aprender a programar de manera estructurada en python
* Alcanzar un pensamiento computacional 
* Incrementar el nivel de abstracción
* Contar con las bases necesarias para seguir avanzando en el mundo de la programación

## Requerimientos de software
Visita la página de [requerimientos](docs/Requirements.md) para que instales todo lo que necesitas

## Un vistazo al IDE y la consola <a name="terminal"></a>
### Abrir una terminal
#### Usuarios windows - Run command
```
python --version
```
#### Usuarios mac o linux - Run command
```
python3 --version
```
#### Ejecutar python (abre la consola)
```
python
```
#### Para salir de la consola
```
exit()
```
## Operadores aritméticos <a name="arithmetic_operators"></a> 
### Dentro de la consola de python, verifica e identifica los siguientes operadores básicos
```python
2 + 3
2 - 3
3 * 4
10 // 3
10 / 3
5 % 2
2 ** 5
```
### Precedencia de operadores básicos
```python
1.- () # Paréntesis 
2.- ** # Exponente
3.- * / // % # Multiplicación, división, división entera y módulo (misma precedencia)
4.- + - # Suma y resta (misma precedencia)
```
*Cuando encuentres operadores que tienen la misma precedencia, resulve de izquierda a derecha siempre*<br>
#### ¿Cuál es el resultado de las siguientes expresiones?
1. `(5 - 1) * ((7 + 9) / (3 - 1)) = ?`
2. `5 - 1 * 7 + 9 / 3 - 1 = ?`
3. `5 + 10 // 4 * 8 % 3 * 2 ** 3 = ?`
*Verifica tus resultados en la consola de python

## Hola mundo en python <a name="hello_world"></a>
1. Crea una carpeta de trabajo
2. Dentro de la carpeta de trabajo, crea el archivo 01_HolaMundo.py 
3. Coloca el siguiente código
```
print ("Hola mundo")
```
4. Desde la terminal ejecuta el programa
```
python 01_HolaMundo.py 
```
*Verifica su funcionamiento

## ¿Qué sucede internamente cuando se ejecuta `python 01_HolaMundo.py` <a name="what_happening"></a>
1. El sistema operativo busca el archivo 01_HolaMundo.py en el sistema de archivos.
2. Si se encuentra el archivo 01_HolaMundo.py, el sistema operativo carga el **intérprete de Python** y le pasa el archivo .py para su ejecución.
3. El intérprete de Python **compila** el archivo .py a **bytecode**, que es una forma intermedia del código que se ejecuta más rápido que el código fuente.
4. Si el intérprete de Python encuentra errores de sintaxis o de tiempo de ejecución, muestra un mensaje de error al usuario.
5. Si el archivo .py se ejecuta sin errores, el **intérprete de Python comienza a ejecutar el bytecode del archivo**. El intérprete de **Python lee cada línea de código** y ejecuta las instrucciones correspondientes.
6. Cuando se termina la ejecución del archivo .py, el intérprete de Python se cierra y libera cualquier recurso que haya utilizado.

## Comentarios <a name="comments"></a>
Los comentarios, son líneas dentro de nuestro código y que sirven para documentar nuestro código, éstas líneas no son consideradas en la compilación por python. 
```python
# Comentarios de una sola línea
""" 
Comentarios multilinea
Por ejemplo, aquí tenemos 2 líneas
"""

'''
También se puede utilizar
la comilla simple (3 veces) para indicar un comentario multilinea
'''
```
## Variables y Tipos de datos <a name="data_type"></a>
* Una variable es la representación de un *dato* almacenado en la memoria dinámica *(RAM)*
* Un nombre de variable no puede comenzar con un número
* Un nombre de variable tiene que comenzar con una letra o el carácter de subrayado
* Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _).
* Case sensitive: Los nombres de las variables distinguen entre mayúsculas y minúsculas (hola, Hola y HOLA son tres variables diferentes)

### Tipo Integer
```python
# Un dato entero puede ser: 23, -4, 129 ... 
edad = 47 # Variable 
```

### Float
```
# Un dato flotante puede ser: -1.23, 45, 987.342 ... 
estatura = 1.7
```

### String
```python
nombre = "Francisco"    # string de una sola línea
apellido = 'Vázquez'    # string de una sola línea
resumen =               # string multilinea
    """ 
        ==> Profresor de cátedra
        ==> Investigador

    """
```
#### Verifica lo siguiente en la consola de python
```python
# Concatenación
"Hola" + 'amigo' 
'Hola '*10
# Error
"Hola" + 5
# Corrección - Casting
"Hola" + str(5)
```

### Tipado dinámico
Seguro que ya notaste que la sintaxis de python es muy *directa*, no se requiere definir un *tipo de dato*, por lo que una variable puede cambiar su tipo de dato almacenado en tiempo de ejecución, por ejemplo: 
```python
nombre = "Francisco"    # La variable nombre almacena un string
nombre = 74.5           # La variable nombre almacena un flotante
nombre = 20             # La variable nombre almacena un entero
nombre = True           # La variable nombre almacena un booleano 
```
*Si requieres conoecer el tipo de dato puedes hacerlo con `type(variable)`

### Casting
El cast o casting permite convertir un tipo de datos a otro tipo de datos distinto. 
```python
x = int(3) # ==>  3
y = int(3.6) # ==>  3
z = int("3") # ==>  3

x = float(3) # ==>  3.0
y = float(3.1) # ==>  3.1
z = float("3") # ==>  3.0
w = float("3.5") # ==>  3.5

x = str("d4") # ==> 'd4'
y = str(3) # ==> '3'
z = str(5.0) # ==> '5.0'
```

## input - keyboard <a name="input_keyboard"></a>
```python
nombre = input()            # Espera un string desde teclado 

print('Teclea un número: ')
edad_str = input()          # Se pide un número (Todo entra como string)
edad = int(edad_str)        # Se convierte a número 

edad = int(input('Teclea un número: '))  # Lo mismo en una sola línea 
```

## Ejercicios - Básicos <a name="basic_exercise"></a>
Realiza los siguientes ejercicios: 
* 00HelloWorld
* 01OperacionesBasicas
* 02AreaTriangulo
* 03Promedio
* 04CalculaTiempo

## String - funciones <a name="string_functions"></a>
* La función `print()` se utiliza para pintar el texto de la cadena
### String = Lista de caracteres
```python
x = 'Python' 
print(x[2]) # ==> t  - Observa que las posiciones en la lista empiezan en CERO 
```

### String = Slicing
```python
x = 'Python es lo mejor' 
print(x[4:8]) # ==> on e  - Observa que el límite inferior se incluye, sin embargo, el límite superior no
print(x[:3]) # ==> Pyt 
```

### String len 
```python
x = 'Python' 
print(len(x)) # ==> 6 
```

### String strip 
```python
x = '  Python es lo mejor  ' 
print(x.strip()) # ==> Python es lo mejor
```

### String replace 
```python
x = 'Python es lo mejor' 
print(x.replace('o','x')) # ==> Pythxn es lo mejxr
print(x) # Observa que la variable x, NO fue modificada 
```

### String Otras funciones
* lower()
* upper()
* isupper()
* islower()






 Sentencias de control, Ciclos, Tuplas, Listas, Matrices, Diccionarios, Funciones, Archivos, Excepciones, Estadística básica, Gráficas, Estándares de programación PEP-8, Entorno virtual. 