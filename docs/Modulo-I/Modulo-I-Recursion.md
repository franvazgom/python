<img src="../../images/LogoMagicPython.png" width="100">

# Recursividad
La recursividad, es una técnica de programación. (divide el problema en problemas mas pequeños) <br>
La recursividad, nos permite que un bloque de instrucciones se ejecute un cierto número de veces (el que nosotros determinemos). <b>
La recursividad la podemos ver como un concepto en programación que se refiere a la capacidad de una función para llamarse a sí misma durante su ejecución. En otras palabras, una función recursiva es aquella que se llama a sí misma para resolver un problema al dividirlo en subproblemas más pequeños. <br>

## Estructura de una función recursiva 

### Caso Base
Siempre debe existir un caso base, es el momento en el que se "rompe" la recursión 

### Caso Recursivo 
Es el caso donde se llama a si misma la función, siempre con el objetivo de acercarnos al caso base. 

### Memoria
Cuando se realiza una llamada recursiva, la memoria se comporta de manera diferente a las llamadas regulares de funciones. Cada vez que se realiza una llamada recursiva, se crea una nueva instancia de la función en la memoria, lo que se conoce como "pila de llamadas" o "pila de ejecución". Esta pila almacena información como los parámetros de la función y la ubicación en el código donde se debe reanudar la ejecución después de que se complete la llamada recursiva. El puntero de la pila se conoce como `stack pointer` <br>

### Límite de llamadas recursivas
En python para conocer el límite de llamdas permitidas, se utiliza la función `sys.getrecursionlimit()` <br>

En python para modificar el límite de llamdas permitidas, se utiliza la función `sys.setrecursionlimit()` <br>

## Ejemplo de función recursiva 

```python

def funcion_recursiva(n):
    if n <= 1:                              # Caso base
        print('Termina la recursión.')
    else:
        print("Se ejecuta una llamada recursiva")
        return funcion_recursiva(n-1)       # Caso recursivo 


def main():
    # ¿Qué hace el siguient ecódigo? 
    funcion_recursiva(5)
    
```

