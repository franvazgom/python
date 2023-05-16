

def main():
    nombre = input("Teclea tu nombre: ")
    nombre = nombre.strip().upper()
    if nombre == 'Alicia'.upper():
        print("Hola Alicia")
        print("Saludos ALICIA!!!")
    else:
        print("Hola extraño")
    if "a".upper() in nombre.upper():
        print("Tu nombre contiene al menos una A")
    
    print("Final del programa") 
    print("Adios")


if __name__ == '__main__':
    main()
