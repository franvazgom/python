import math


def main():
    str1 = f'1.- El valor de Pi = {math.pi}'
    print(str1)
    print(f'2.- El valor de Pi a 4 decimales es: {math.pi:.4f} ')
    x = 3.56
    print(f'x = {round(x,1)}')

    print('*'*50)
    nombre1 = 'Francisco'
    apellido1 = 'Vázquez'
    edad1 = 47

    nombre2 = 'Laura'
    apellido2 = 'Fer'
    edad2 = 5

    print("Datos sin formato")
    print(nombre1, apellido1, edad1)
    print(nombre2, apellido2, edad2)
    print('*'*50)

    print("Datos con formato")
    print('-'*37)
    print(f'-{"Nombre":15}{"Apellido":15}{"Edad":5}-')
    print('-'*37)
    print(f'-{nombre1:15}{apellido1:15}{edad1:5}-')
    print(f'-{nombre2:15}{apellido2:15}{edad2:5}-')
    print('-'*37)

    # print(F"Hola {'cadena':23} mundo")

if __name__ == '__main__':
    main()
