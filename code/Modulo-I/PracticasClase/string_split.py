def main():
    original = "Hola, México - Felicidades!!"
    x = original.split()    # Divide al string cada vez que encuentra un espacio 
    print(x[0])
    print(x[3][4])          #Debe imprimir la c de la cadena Feliciades!! 

    print('-'*50)

    lista = ["Hola", "Mexico", "Saludos"]
    cad = ' '.join(lista)
    print(cad)

    print('-'*50)

    


if __name__ == '__main__':
    main()
