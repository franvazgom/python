<img src="../../images/LogoMagicPython.png" width="100">

# Python - Sentencias de control

## Operadores de comparación y su precedencia

## Diagramas de flujo 
<img src="../../images/DiagramaFlujoIF.png" width="800">

## Operadores y su precedencia
<img src="../../images/OperatorsPrecedencia.png" heigh="200">

## Tablas de verdad del `and` y `or`
<img src="../../images/TablasVerdad.png" heigh="350">

## Ejemplos de expresiones
```python
    >>> "Hola" == "hola"
    False
    >>> 34 > 12.5
    True
    >>> 12 <= 12
    True
    >>> not True
    False
    >>> 4 < 6 and 2 > 3 
    False
    >>> 4 < 6 or 2 > 3
    True
    >>> "desde" not in "Hola desde México"
    False
    >>> nombre = 'Juan'
    >>> edad = 21
    >>> nombre == 'Juan' and edad >= 18
    True
```


## Ejemplo If
<img src="../../images/IfEjemplo1.png" width="600">

```python
    if name == 'Alice':  
        print ("Hello Alice.")  # inicia un bloque, notar la indentación (sangría)
    else:
        print ("Hello stranger.)
```

## Bloques de código
Las líneas de código de python pueden ser agrupadas en bloques, las reglas de un bloque son: <br>
1. Un bloque inicia cuando la indentación crece
2. Un bloque puede contener otro bloque de código
3. Un bloque termina cuando la indentación decrece


## Ejemplo If (bloques)

```python
    if name == 'Alice':  
        print ("Hello Alice.")  # Inicia el bloque
        print ("Welcome")       # Fin del bloque
    # Observa que el `else` no es obligatorio 
    print("Hi!!!! ... ")        # Esta instrucción no es parte del bloque
```
## Ejemplo elif 
<img src="../../images/IfElIfEjemplo1.png" width="600">


## Ejemplo elif complejo
<img src="../../images/IfElIfEjemplo2.png" width="600">

### ¿El órden es importante?