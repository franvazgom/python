'''
Escribiendo un archivo
lines = ['linea 1', 'Línea 2', 'linea 3']
    with open('salida.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
'''
import os
def main():
    # Escribe tu código abajo de esta línea
    path = os.path.dirname(__file__)
    lines = ['frase 1 otras cosas.. comunicación', 'Segunda frase..', 'frase numero 3']
    with open(path + '/../../../files/datos_salida.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
