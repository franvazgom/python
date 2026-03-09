'''
Indicadores de tipo en funciones
==================================

Python permite una sintaxis auxiliar para indicar el tipo de dato esperado para un parámetro en una función, así como el tipo de dato retornado por la función:
* Es una sintaxis meramente auxiliar para el programador.
* Así el programador puede ver que tipos de datos se esperan para los parámetros de una función, sin tener que revisar el código o la documentación.
* El intérprete ignora completamente los indicadores de tipo, por lo que la función se puede invocar con cualquier tipo de dato distinto al indicado

Sintaxis:
----------

* Para indicar el tipo de dato esperado para un parámetro, la sintaxis es: `parametro:tipo_esperado`
    * Ejemplo, elevar 5 a una pótencia dada: `elevar_5(potencia:int):`
* Además del tipo esperado también podemos establecer un valor por defecto con la sintaxis: `parametro:tipo_esperado=valor_defecto`
    * Ejemplo, la potencia por defecto será 2: `elevar_5(potencia:int=2):`
* Cada parámetro puede llevar su indicador: 
    * `elevar(base:float, potencia:int):`
* Se puede indicar también el tipo de dato que retornará la función con `->`:
    * `elevar(base:float, potencia:int) -> float:`
    * `procesar(datos:list) -> None:`
* Se puede indicar varios tipos de dato esperados o retornados, separándolos con la barra `|`:
    * Ejemplo: `elevar(base:float|int, potencia:int) -> float|int:`
    * La barra solo funciona desde Python 3.10 en adelante.
    * Anteriormente se hacía con: `Union[float, int]`
'''

##############################################################################
# Definiciones
import os

ruta_carpeta = os.path.dirname(__file__)

# Indicamos un tipo de dato esperado en el parámetro
def duplicar_texto(texto:str):
    return texto * 2

# Indicamos dos tipos de dato esperados para cada parámetro y para el retorno
def sumar_numeros(a:int|float, b:int|float) -> int|float:
    return a + b

# Solo especificamos tipos esperados para un parámetro
def multiplicar_numeros(a:int|float, b) -> int|float:
    return a * b

# None también puede ser un tipo esperado y podemos asignar un valor 
# por defecto al parámetro, en este caso el valor por defecto es None
def cargar_texto(ruta_archivo:str|None=None) -> str:
    if ruta_archivo is None:
        ruta_archivo = ruta_carpeta + "\\archivo_default.txt"
    
    with open(ruta_archivo, "r") as archivo:
        return archivo.read()


def elevar(a:int, n:int=2):
    return a ** n

def sumar(a, b=2, c=3, d=4, e=5):
    return a + b + c + d + e
