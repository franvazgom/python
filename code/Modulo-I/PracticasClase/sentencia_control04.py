

def main():
    edad = int(input("Teclea tu edad: "))
    if edad < 3:
        print('Eres un bebe')
    elif edad < 5:
        print('Eres un infante')
    elif edad < 12:
        print('Eres un niño')
    elif edad < 19:
        print('Eres un adelocente')
    elif edad < 35:
        print('Eres un joven')
    elif edad < 60:
        print('Eres un adulto')
    elif edad < 100:
        print('Eres un anciano')
    else:        
        print('Eres un vampiro')

if __name__ == '__main__':
    main()
