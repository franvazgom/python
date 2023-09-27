'''
Práctica: 
Crear un programa que implemente la función "fibonacci" la cual debe ser recursiva
Recuerda que el número 'n' de la serie de fibonacci se calcula con la suma de los dos anteriores, 
también ten en cuenta que los dos primeros números de la serie son 0 y 1 

Ejemplo de la serie: 
0,  1,  1,  2,  3,  5,  8,  13,  21, 34 ... 
Ejemplos: 

El número 6 de la serie, 
fibonacci(6) = 8 (empezando desde la posición 0)

El número 7 de la serie, 
fibonacci(7) = 13 (empezando desde la posición 0)

'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Programa que calcula número 'n' de la serie de fibonacci")
    n = int(input('n => '))
    resultado = fibonacci(n)
    print(f'El número fibonacci de {n} = {resultado}')

if __name__ == '__main__':
    main()