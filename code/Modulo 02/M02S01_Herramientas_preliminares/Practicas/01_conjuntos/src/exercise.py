'''
Conjuntos
================================================

Los `conjuntos` en Python son una estructura para simular conjuntos 
matemáticos:
* No almacenan duplicados
* Sus elementos deben ser hashables como las llaves de un diccionario
* Al igual que con las listas, sus elementos puedens ser de tipo mixto

Entre las operaciones que soportan están:
* Pertenencia: si un elemento está en un conjunto
    * Operadores: `in` y `not in`
* Subconjunto: un conjunto contiene todos los elementos de otro conjunto
    * Operadores: `<=` y `>=`
* Subconjunto propio: un conjunto es subconjunto de otro pero no son iguales
    * Operadores: `<` y `>`
* Uniones: unir los elementos de dos o más conjuntos
    * Operadores: `|`
* Intersecciones: obtener los elementos que existen en dos o más conjuntos
    * Operadores: `&`
* Diferencia: a un conjunto quitarle los elementos que también estén en otro
    * Operadores: `-`
* Diferencia simétrica: obtener los elementos que están solo en uno de dos conjuntos, pero no en los dos
    * Operadores: `^`

Sintaxis:
---------
* Para definir un conjunto es similar a las listas, solo que en lugar de usar
  los corchetes `[]`, en este caso se usan llaves `{}`.
* Se puede definir un conjunto vacío con `set()`
* Se puede convertir cualquier iterable `I` a conjunto con `set(I)`, 
  tengamos en cuenta que esto elimina los duplicados.
'''

##############################################################################
# Definiciones

# Conjunto de los números del 1 al 10
# Aunque tenemos elementos repetidos, solo se almacenan los elementos únicos
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 5, 7}
# Conjunto de los números del 6 al 15
B = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# Conjunto de los números del 4 al 9
C = {4, 5, 6, 7, 8, 9}
# Conjunto de textos
productos = {"RAM", "SSD", "CPU"}
# Conjunto mixto
mixto = {"1.42", "43", "342.2", 1.3434, 232}
# Un conjunto vacío
vacio = set()
# Conjunto a partir de lista
conjunto_de_lista = set([1,3,4,5,6,1,2,3])
# Conjunto a partir de tupla
conjunto_de_tupla = set(("1","3","4","5","6","1","2","3"))

##############################################################################
# Operaciones

# Podemos revisar si un elemento pertenece a un conjunto
print(f"SSD está en productos: {'SSD' in productos}")

# Podemos confirmar que C es subconjunto de A
print(f"C subconjunto de A: {C <= A}")
# Pero no alrevez
print(f"A subconjunto de C: {A <= C}")

# La intersección de A con B: {6, 7, 8, 9, 10}
print(f"A intersección con B: {A & B}")

# La unión de A con B: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(f"A unión con B: {A | B}")

# La diferencia de A con B: {1, 2, 3, 4, 5}
print(f"A - B: {A - B}")
# La diferencia de B con A: {11, 12, 13, 14, 15}
print(f"B - A: {B - A}")

# La diferencia simétrica de A con B: {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}
print(f"A ^ B: {A ^ B}")

##############################################################################
# Ejemplos de uso

# Para saber si todos los elementos de una lista `X` están contenidos
# en otra lista `Y`, lo que normalmente haríamos sería algo como lo siguiente
def estan_todos(X, Y):
    for c in X:
        if c not in Y:
            return False
    
    return True

# Usando conjuntos esto se simplifica de la siguiente forma
def estan_todos_set(X, Y):
    return set(X) <= set(Y)

# Ambas funciones realizan lo mismo, como vemos a continuación
S = [2,3,5]
T = [1,2,3,4,5]
print(f"[2,3,5] están en [1,2,3,4,5]: {estan_todos(S, T)}")
print(f"[2,3,5] están en [1,2,3,4,5]: {estan_todos_set(S, T)}")
print(f"[1,2,3,4,5] están en [2,3,5]: {estan_todos(T, S)}")
print(f"[1,2,3,4,5] están en [2,3,5]: {estan_todos_set(T, S)}")

##############################################################################
