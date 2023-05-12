import math

# String format 
# Expresión con prefijo f o F  { expression }

str1 = f'1.- El valor de PI = {math.pi}'
print(str1)
print(f'2.- El valor de PI = {math.pi:.4f}')

# entero después de : completa el número de caracteres la amplitud del string

nombre1 = 'Francisco'
apellido1 = 'Vazquez'
edad1 = 47

nombre2 = 'Laura'
apellido2 = 'Fer'
edad2 = 7

print()
print (f'{"Nombre":15}{"Apellido":15}{"Edad":6}')
print (f'{nombre1:15}{apellido1:15}{edad1:6}')
print (f'{nombre2:15}{apellido2:15}{edad2:6}')
print()



