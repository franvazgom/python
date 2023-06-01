'''
Práctica: 
Crear un programa que implemente la función "factorial" la cual debe ser recursiva
Recuerda que el factorial solo es válido para n >= 0  y que el factorial(0) = 1 
'''

def factorial(n):
    pass

def main():
    print("Programa que calcula el factorial de un número de manera recursiva")
    n = int(input('n => '))
    resultado = factorial(n)
    print(f'El factorial de {n} = {resultado}')

if __name__ == '__main__':
    main()