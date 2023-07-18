
datos = [
    ['Poblacion', '01/01/2020', '02/01/2020', '03/01/2020', '04/01/2020', '01/02/2020', '02/02/2020', '03/02/2020'],
    ['Mexico', 34, 23, 56, 22, 12, 43, 100],
    ['Puebla', 12, 56, 98, 23, 31, 65, 77]
]

def obtiene_datos_por_mes(datos):
    f = 1 # Mexico
    '''Datos esperados
    mes = ['01/2020', '02/2020']
    acumulado = [135, 155]
    ''' 
    datos_mes = []
    acumulado = []
    mes_actual = ""
    suma = 0
    for i in range(1, len(datos[0])):
        fecha = datos[0][i]
        mes = fecha[3:]
        if mes != mes_actual: #Cambio de mes
            datos_mes.append(mes)
            acumulado.append(suma)
            suma = 0
            mes_actual = mes
        suma += datos[f][i]
    datos_mes.append(mes)
    datos_mes = datos_mes[1:]
    acumulado.append(suma)
    acumulado = acumulado[1:]
    return [datos_mes, acumulado]

def main(): 
    # x = obtiene_datos_por_mes(datos)
    # print(x)

    ciudad = '"MEXICO"'
    ciudad = ciudad[1:len(ciudad)-1]
    print(ciudad)


if __name__ == '__main__':
    main()
