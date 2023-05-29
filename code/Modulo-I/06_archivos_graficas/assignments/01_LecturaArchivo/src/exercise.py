'''
Leyendo un archivo
Probando el método readlines
with open('datos.csv', 'r') as f:
        lines = f.readlines()
¿Qué  hace?

¿Es necesario cerrar el archivo?

Ruta:
os.path.dirname(__file__)

¿Cómo lo guardo en una matriz?

otra forma..   readline()
with open('datos.csv', 'r', encoding='utf-8') as f:
        linea = True        
        while linea:
            linea = f.readline()
'''


import os
def main():
    # Escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()