
# Una buena práctica, el uso de la variable __name__ 
def main():
    print("Hola mundo")

# La variable __name__ toma su valor dependiendo de como se ejecute el script,
# cuando el valor de la variable es: __main__ python indica que el script 
# principal es 'este script' 
if __name__ == '__main__':
    main()