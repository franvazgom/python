

def main():
    name = ''
    while True:
        name = input("Teclea tu nombre:")
        if name != 'Joe':
            continue    #Rompe la iteración actual 
        print("Hola Joe")
        password = input("Teclea tu password:")
        if password == "swordfish":
            break       #rompe el ciclo
        print("No es la contraseña... lo siento :( ")
    print("Se rompio el ciclo")
if __name__ == '__main__':
    main()