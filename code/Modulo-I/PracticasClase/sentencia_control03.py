

def main():
    nombre = input("Teclea tu nombre: ")
    nombre = nombre.strip().upper()
    edad = int(input("Teclea tu edad: "))

    if nombre == 'Alicia'.upper():
        print("Hola Alicia")
    elif edad < 12:             #If encadenado 
        print("Tu no eres Alicia, pero si eres menor de 12")
    else:
        print("Tu no eres Alicia y tampoco eres menor de 12")


if __name__ == '__main__':
    main()
