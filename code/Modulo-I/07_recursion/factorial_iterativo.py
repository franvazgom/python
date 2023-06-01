'''
Práctica: 
Crear un programa que implemente la función "factorial" la cual debe ser iterativa, 
es decir, puedes utilizar un ciclo for o un ciclo while 
Recuerda que el factorial solo es válido para n >= 0  y que el factorial(0) = 1 
'''

def factorial(n):
    pass

def main():
    print("Programa que calcula el factorial de un número de manera iterativa")
    n = int(input('n => '))
    resultado = factorial(n)
    print(f'El factorial de {n} = {resultado}')

if __name__ == '__main__':
    main()