# Python PEP 8: (Python Enhancement Proposal) Código fácil de leer
## Introducción
* Mejora la legibilidad del código: El código es más fácil de leer y entender.
* Facilita la colaboración: Los equipos pueden trabajar juntos más fácilmente si siguen un estilo común.
* Facilita el mantenimiento del código: El código consistente es más fácil de mantener y actualizar.

### Indentación
+ Usa 4 espacios por nivel de indentación.
### Longitud Máxima de Línea:
+ Limita todas las líneas a un máximo de 79 caracteres.
+ Para las docstrings o comentarios, limita a 72 caracteres.
```python
# Correcto
def mi_funcion(primer_parametro, segundo_parametro,
               tercer_parametro, cuarto_parametro,
               quinto_parametro):
    print("Python")

# Incorrecto
def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro, cuarto_parametro, quinto_parametro):
    print("Python")

# Correcto
with open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/linea/') as fichero_1, \
     open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/linea/', 'w') as fichero_2:
    fichero_2.write(fichero_1.read())

# Recomendado
income = (variable_a
          + variable_b
          + (variable_c - variable_d)
          - variable_e
          - variable_f)

# No recomendado
income = (variable_a +
          variable_b +
          (variable_c - variable_d) -
          variable_e -
          variable_f)

```

### Líneas en Blanco
+ Usa dos líneas en blanco antes de las definiciones de funciones y clases a nivel de módulo.
+ Usa una línea en blanco para separar secciones lógicas dentro de una función.
+ Dejar una línea en blanco entre los métodos de una clase. 
```python
# 1 espacio entre métodos
# 2 espacios entre clases y funciones
class ClaseA:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


class ClaseB:
    def metodo_a(self):
        pass

    def metodo_b(self, valores):
        # Calculamos la media
        suma_valores = 0
        for valor in valores:
            suma_valores += valor
        media = suma_valores / len(valores)
        
        # Calculamos la mediana
        valores_ordenados = sorted(valores)


def funcion():
    pass
```
### Importaciones
+ Coloca todas las importaciones al comienzo del archivo.
+ Ordena las importaciones en bloques separados: importaciones estándar de la biblioteca, importaciones de terceros y luego importaciones locales.
+ Usa una línea en blanco entre cada bloque de importación.
```python
import os
import sys

import numpy as np

from mymodule import myfunction
```
### Espacios en Blanco en Expresiones y Sentencias
+ Evita espacios en blanco innecesarios.
+ Usa espacios alrededor de los operadores y después de las comas, pero no dentro de las llaves de indexación.
```python
# Correcto
x = 5

# Incorrecto
x=5

# Correcto
a = b + c
my_list = [1, 2, 3]

# Incorrecto
a=b+c
my_list = [ 1, 2, 3 ]

# Valores por defecto, Correcto
def mi_funcion(parameto_por_defecto=5):
    print(parameto_por_defecto)

# Incorrecto
def mi_funcion(parameto_por_defecto = 5):
    print(parameto_por_defecto)

# No dejar espacio entre paréntesis
# Correcto
duplica(2)

# Incorrecto
duplica( 2 )

# Correcto
lista = [1, 2, 3]

# Incorrecto
my_list = [ 1, 2, 3, ]

# Correcto
if x > 0 and x % 2 == 0:
    print('...')

# Correcto
if x>0 and x%2==0:
    print('...')

# Incorrecto
if x% 2 == 0:
    print('...')

# Correcto
lista[0]

# Incorrecto
lista [1]

# Incorrecto
lista [ 1 ]

# Correcto
var_a = 0
variable_b = 10
otra_variable_c = 3

# Incorrecto
var_a           = 0
variable_b      = 10
otra_variable_c = 3
```
### Nombres de Variables y Funciones
+ Usa nombres de variables y funciones en minúsculas con palabras separadas por guiones bajos.
+ Usa nombres de clases en estilo CamelCase.
+ Variables: Al igual que las funciones: variable, mi_variable.
+ Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.
+ Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.
+ Constantes: Nombrarlas usando mayúsculas y separadas por barra bajas: UNA_CONSTANTE, OTRA_CONSTANTE.
+ Módulos: Igual que las funciones: modulo.py, mi_modulo.py.
+ Paquetes: En minúsculas pero sin separar por barra bajas: packete, mipaquete

```python
# Variables y funciones
def my_function():
    my_variable = 10

# Clases
class MyClass:
    pass

# Constantes
MAX_LIMIT = 100
```
### Documentación
+ Usa docstrings para documentar todas las funciones, clases y módulos públicos.
+ Coloca la docstring justo después de la definición de la función o clase.
```python
def my_function(param1, param2):
    """
    Esta función hace algo interesante.

    :param param1: Descripción del primer parámetro.
    :param param2: Descripción del segundo parámetro.
    :return: Descripción del valor de retorno.
    """
    return param1 + param2
```
### Comparaciones con None
+ Usa is y is not para comparar con None.
```python
if my_var is None:
    pass

if my_var is not None:
    pass
```
### Uso de Comillas
+ Usa comillas simples o dobles de manera consistente para las cadenas. PEP 8 no dicta una preferencia específica, pero se recomienda ser consistente dentro de un proyecto.
```python
my_string = "Hello, World!"
another_string = 'Python is great!'
```
## Referencias
[Referencia - PEP8](https://peps.python.org/pep-0008/)

