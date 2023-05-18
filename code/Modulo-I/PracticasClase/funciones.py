   
def saluda():
    print("Hola a todos")
    print('adios')

def saluda2(nombre):
    print(f'Hola {nombre} ¿Cómo estas?')
    print('adios')    

def suma(num1, num2):
    print("Esta funcion realiza una suma..")
    resultado = num1 + num2
    return resultado

def concatena_n_veces(palabra, n):
    if n % 2 == 0:
        print(palabra * n)
    else:
        print(palabra)

def main():
    # saluda()
    # saluda2('Paco')
    # dato = input("Teclea tu nombre: ")
    # saluda2(dato)
    # r1 = suma(2, 50.4)
    # print(f'El resultado es: {r1}')
    # r2 = suma("Hola", str(23))
    # print(f'El resultado es: {r2}')
    # x = saluda()
    # print(".......")
    # print(x)
    # print(".......")
    # concatena_n_veces('Prueba ',4)
    # concatena_n_veces(50, 'prueba')
    #No importa el orden cuando se nombran los argumentos
    concatena_n_veces(n=4, palabra='Prueba ')
    



if __name__ == '__main__':
    main()