ham = 100   #Variable GLOBAL


def spam():
    eggs = 3132 # Variable LOCAL a la función spam
    ham = 34    # Variable LOCAL a la función spam
    print(eggs)
    bacon()
    print(eggs, ham)

def bacon():
    global ham      # Hace referencia a la variable GLOBAL ham
    eggs = 99       # Variable LOCAL a la función bacon
    ham = 88.5      # Se modifica la variable GLOBAL 
    print(eggs)

def main():
    spam()
    print(f'el valor de ham es: {ham}')
    # bacon()
    # print(eggs)


if __name__ == '__main__':
    main()