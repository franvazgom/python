import os

def regresa_suma(matriz):
    res = []
    estados = []
    for i in range(1, len(matriz)):
        fila = matriz[i]
        estados.append(fila[2])
        suma = 0
        for j in range(3, len(fila)):
            cantidad = fila[j]
            suma += int(cantidad)
        res.append(suma)
    return res, estados

def main():
    path = os.path.dirname(__file__)
    datos = []
    with open(path + '/../../../files/datos.csv', 'r') as f:
        linea = True
        while linea:
            linea = f.readline()
            if len(linea) > 0:  # Limpieza de datos.. 
                linea = linea[:-1]  # Se elimina el ultimo enter
                fila = linea.split(',')
                datos.append(fila)
    resultado, estados= regresa_suma(datos)
    print(resultado, estados)



if __name__ == '__main__':
    main()