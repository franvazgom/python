'''
Iterables (listas, conjuntos, diccionarios, etc) por comprensión
=================================================================

Generar iterables por comprensión consiste usar un iterable base para generar otro iterable:
* La idea es tomar el iterable base para crear otro iterable, donde a cada elemento del iterable base se le aplicará una transformación a través de una expresión de Python.
* El iterable resultante no tiene que ser del mismo tipo que el base, es decir, podemos crear una lista a partir de una tupla, o un diccionario a partir de una lista, etc.
* Se le puede aplicar un filtro a la comprensión para solo quedarnos con los elementos que satisfagan las condiciones del filtro

Sintaxis:
---------
* La estructura básica de una comprensión es: `expresion for var in iterable_base`
    * Ejemplo: `[2 * i + 1 for i in range(10)]`
* La estructura agregando un filtro es: `expresion for var in iterable_base if condicion`
    * Ejemplo: `[i for i in range(10) if i % 2 == 0]`
* La estructura de una comprensión con dos iterables base anidados es: `expresion for var1 in iterable_base_1 for var2 in iterable_base_2`
    * Ejemplo: `[(i, j) for i in range(3) for j in range(3)]`
'''

##############################################################################
# Definiciones

import math


# Conjunto de números pares menores a 40
pares_40 = {i for i in range(40) if i % 2 == 0}
# Conjunto de números impares menores a 1000
impares_1000 = {i for i in range(1000) if i % 2 == 1}
# Conjunto de los números que son cuadrados perfectos menores a 1000
cuadrados_1000 = {i * i for i in range(1, math.ceil(math.sqrt(1000)))}
# Conjunto de números menores a 1000 que al dividirlos por 5 sobra 1
cinco_residio_1 = set(range(1, 1000, 5))
# Lista de tuplas (i, j) donde `0 <= i <= 4` y `0 <= j <= 3`
tuplas_cartesianas = [(i, j) for i in range(5) for j in range(4)]

##############################################################################
# Operaciones

# Números pares menores a 40 que no son cuadrados perfectos
pares_no_cuadrados = pares_40 - cuadrados_1000
print(f"Pares menores a 40 que no son cuadrados: {pares_no_cuadrados}")

# Conjunto de los cuadrados perfectos menores que 1000, 
# que además son impares, y al dividirlos por 5 sobra 1.
conjunto_raro = cuadrados_1000 & impares_1000 & cinco_residio_1
print(f"Cuadrados, impares y residuo 1 % 5: {conjunto_raro}")
# Lo mismo pero en una lista ordenados de menor a mayor
print(f"Cuadrados, impares y residuo 1 % 5 (ordenados): {sorted(conjunto_raro)}")

# Lista de tuplas (i, j) donde `0 <= i <= 4` y `0 <= j <= 3` y `i + j == 6`
tuplas_cartesianas_suma_6 = [p for p in tuplas_cartesianas if p[0] + p[1] == 3]
print(f"Tuplas (0<=i<=4, 0<=j<=3) con i+j=6: {tuplas_cartesianas_suma_6}")


