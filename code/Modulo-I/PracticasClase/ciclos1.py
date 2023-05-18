
def imprime_nombre_5_veces(nombre):
    spam = 0
    while spam < 5:
        print(nombre, spam)
        # spam = spam + 1
        spam += 1
    print(f"Se rompio el while, el valor de spam = {spam}")

def tecla_tu_nombre():
    nombre = ''
    while nombre != 'tu nombre':
        print("teclea tu nombre")
        nombre = input()
    print("Gracias!!!")

def prueba_break():
    contador = 1
    while True:
        print(contador)
        if contador >= 10:
            break           #Se rompe el ciclo
        contador += 1



def main():
    # imprime_nombre_5_veces('Pruebas')
    # tecla_tu_nombre()
    prueba_break()
    

if __name__ == '__main__':
    main()