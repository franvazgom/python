'''
Fechas con `datetime` y `calendar`
==================================

Python contiene integrada una librería llamada `datetime` para manipular fechas de manera muy sencilla. Entre sus operaciones soporta:
* Crear fechas a partir de texto.
* Convertir fechas `datetime` a texto en el formato que queramos.
* Sumar días, minutos, segundos, etc. a fechas
* Calcular diferencias de tiempo entre fechas
* Manejo de zonas horarias

Sintaxis:
---------

Los objetos y funciones básicos son:
* `datetime.datetime`: objeto para manipular fechas
* `datetime.timedelta`: objeto para almacenar diferencias de tiempo
* `datetime.datetime.now()`: obtiene la fecha y hora de este momento
* `datetime.datetime.strptime()`: crea una fecha desde texto
* `datetime.datetime.strftime()`: convierte una fecha a texto
'''

##############################################################################
# Definiciones

from datetime import datetime, timedelta

# Obtenemos la fecha y hora de este momento
ahora = datetime.now()
# Eliminamos las horas, minutos, etc y solo consevamos día, mes y año
hoy = ahora.replace(hour=0, minute=0, second=0, microsecond=0)
# Otra forma de obtener la fecha de hoy con cero horas, minutos y segundos
hoy = datetime.combine(ahora, datetime.min.time())
# Obtenemos la fecha de mañana
manana = hoy + timedelta(days=1)
# Creamos un datetime con la fecha de navidad
navidad = datetime.strptime("25/12/2022", "%d/%m/%Y")
# Último día de agosto del 2022
fin_agosto = datetime.strptime("01/09/2022", "%d/%m/%Y") - timedelta(days=1)
# Fecha inicializada con valores numéricos
dia_independencia = datetime(year=2022, month=9, day=16)


##############################################################################
# Operaciones

# Número de días para que llegue navidad
dias_para_navidad = (navidad - hoy).days
print(f"Días para navidad: {dias_para_navidad}")

# Último día de agosto del 2022 en formato "dd/mm/aaaa"
fin_agosto_texto = fin_agosto.strftime("%d/%m/%Y")
print(f"Último día de agosto del 2022: {fin_agosto_texto}")

# Revisar si una fecha está entre hoy y navidad
print(f"Dia de Independencia entre hoy y navidad?: {hoy <= dia_independencia  <= navidad}")

##############################################################################
# Ejemplos de uso

def mes_dias(mes, anio):
    r"""
    Devuelve cuantos días tiene un mes dado.

    Args:
        mes (int): número de mes, 1=Enero, 12=Diciembre
        anio (int): numéro de año
    """
    # Obtenemos el año/mes resultante de movernos un mes adelante
    # Remplazamos los originales porque ya no los necesitaremos
    anio += mes // 12
    mes = (mes % 12) + 1

    # Generamos una fecha con el primer día del siguiente mes
    primer_dia_sig_mes = datetime(year=anio, month=mes, day=1)

    # Restamos un día para quedar en el último día del mes original
    # y devolvemos el número de día correspondiente
    return (primer_dia_sig_mes - timedelta(days=1)).day


def primer_dia_del_mes(mes, anio, indice_dia):
    r"""
    Primer día semanal del mes/año dado. Por ejemplo, obtener la fecha del
    primer Lunes del mes de Noviembre del 2022. El argumento `indice_dia` 
    es el número de día de la semana en cuestión y representa 
    1=Lunes, ..., 7=Domingo.
    """
    # Fecha del primer día del mes en cuestión
    inicio_mes = datetime(year=anio, month=mes, day=1)
    # Obtenemos el índice del día de la semana del primer día del mes
    # 1=Lunes, ..., 7=Domingo
    indice_inicio_mes = inicio_mes.isoweekday()
    # Número de dias para llegar del inicio del mes al días especificado
    diferencia_dias = indice_dia - indice_inicio_mes
    if diferencia_dias >= 0:
        return inicio_mes + timedelta(diferencia_dias)
    else:
        return inicio_mes + timedelta(diferencia_dias + 7)

