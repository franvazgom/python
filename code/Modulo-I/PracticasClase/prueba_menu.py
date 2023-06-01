
def menu():

    opc = 0
    while opc < 1 or opc > 4: 
        print('1.- Cargar datos')
        print('2.- Ver el maximo')
        print('3.- Mostrar tablas')
        print('4.- salir')
        opc = int(input('Teclea opción ==> '))
    return opc

def main():
    opcion = 0
    while opcion != 4:
        opcion = menu()
        print(opcion)

if __name__ == '__main__':
    main()




