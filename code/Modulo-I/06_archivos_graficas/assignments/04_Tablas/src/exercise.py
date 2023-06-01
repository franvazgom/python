'''
1.- Crear la función muestra_tabla que recibe una matriz con los datos y 
una lista con los titulos de las columnas
2.- Preparar el contenedor donde se va a graficar
    fig, ax = plt.subplots(figsize=(10,5))
5.- Graficar  la tabla
    ax.table(cellText=data, colLabels=column_labels, loc="center")
6-  Mostrar la tabla
    plt.show()
7.- verifica los métodos de ax:
    axis('tight')
    axis('off')
'''
from matplotlib import pyplot as plt

def muestra_tabla(datos):
    fig, ax = plt.subplots(figsize=(6,3))
    column_labels = ['Estado', 'Calificación']
    ax.table(cellText=datos, colLabels=column_labels, loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()

def main():
    # Escribe tu código abajo de esta línea
    matriz = [['Aguascalientes', 98], ['Ciudad de México', 34], ['Puebla', 56]]
    muestra_tabla(matriz)

if __name__ == '__main__':
    main()
