'''
Práctica: 
Crear un programa que implemente la función "factorial" la cual debe ser recursiva
Recuerda que el factorial solo es válido para n >= 0  y que el factorial(0) = 1 
'''
import sys
def factorial(n):
    print(f'El valor de n es: {n}')
    if n == 0 or n == 1:    # Caso Base
        return 1
    else:                   # Caso recursivo , n > 1
        return n * factorial(n+1)

def main():
    print("Programa que calcula el factorial de un número de manera recursiva")
    n = int(input('n => '))
    resultado = factorial(n)
    print(f'El factorial de {n} = {resultado}')

if __name__ == '__main__':
    main()