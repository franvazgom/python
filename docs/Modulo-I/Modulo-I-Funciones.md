<img src="../../images/LogoMagicPython.png" width="100">

# Python - Funciones

En Python, una función es un bloque de código reutilizable que realiza una tarea específica. Las funciones toman un conjunto de entradas, llamadas argumentos o parámetros, realizan operaciones en esos valores y devuelven un resultado o realizan una acción.

Las funciones en Python se definen utilizando la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener los argumentos de la función. A continuación, se especifica un bloque de código indentado que constituye el cuerpo de la función. Aquí tienes un ejemplo básico de cómo se define una función en Python


```python
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

def saludar(nombre):
    print("¡Hola,", nombre, "!")
```
En este ejemplo, se define dos funciones llamadas hello y saludar que toma un argumento nombre. Cuando la función es llamada, imprime un saludo utilizando el valor del argumento nombre. La función se puede llamar en cualquier parte del programa de la siguiente manera

```python
hello()
saludar("Juan")
```

Las funciones pueden tener múltiples argumentos separados por comas, y pueden tener un valor de retorno utilizando la palabra clave return. Además, las funciones pueden ser definidas con argumentos opcionales o argumentos con valores predeterminados.

Las funciones son una parte fundamental de la programación en Python, ya que permiten organizar y reutilizar el código de manera eficiente, facilitando el mantenimiento y la legibilidad del programa.

## return 
En python se utiliza la palabra `return` para regresar uno o varios valores en una función 

```python
    import random

    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Ask again later'
        elif answerNumber == 6:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'My reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'
    
    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)
```

## None
En python, la ausencia de valor se representa con la palabra `None`

```python
valor = print('Hola')
print(valor == None)

```

## Variables locales y globales
### Las variables locales no tienen un alcance global

```python
def spam():
    eggs = 31337
spam()
print(eggs)     # Error
```

```python
def spam():
    eggs = 99   # Variable local a la función spam 
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0    # Variable local a la función bacon

spam()
```

### Variable global, alcance

```python
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
```


### Variable global y local con mismo nombre 

```python
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
```

### Variable global y local con mismo nombre 

```python
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
```

```python
def spam():
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)        # prints 'global'
```


### sentencia `global`

```python
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
``` 