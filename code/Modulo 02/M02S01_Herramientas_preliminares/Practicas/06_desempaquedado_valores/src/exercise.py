'''
Desempaquetado de valores y de parámetros
================================================

Python tiene un mecanismo que simplifica el manejo de valores contenidos en una lista o tupla:
* El mecanismo consiste en separar los valores de una lista o tupla de manera muy sencilla

Sintaxis:
----------

* Podemos asignar los valores de una lista a variables con: `var1, var2, ..., varN = lista`
    * En este caso el número de variables debe ser igual a los elementos en la lista
* Si queremos separar solo los primeros valores y el resto dejarlos en una lista: `var1, var2, ..., vark, *restante = lista`
    * Así los primeros `k` valores serán asignados a las primeras variables, y el resto de elementos será asignado a una lista cuyo nombre debe estar al final precedido por un arterisco `*`.
* Para desempaquetar los valores de una lista y usarlos como parámetros separados de una función: `funcion(*lista)`
    * Así cada elemento de la lista se enviará como parámetro a la función en en mismo orden en el que están en la lista.
'''

##############################################################################
# Definiciones

# Nombres de columnas
columnas = ["Precios unitarios", "Cantidades en existencia"]
# Datos geográficos
datos_geo = [19.239805, -103.709148, "06", "002", "0001"]

def procesar_datos(lat, lng, edo, mun, loc):
    # Asumimos que aquí se hace un procesamiento
    print("\nProcesando datos")
    print(f"{lat=}", f"{lng=}", f"{edo=}", f"{mun=}", f"{loc=}")

##############################################################################
# Operaciones

# Separamos los nombres de columnas en identificadores más claros
col_precios, col_existencias = columnas
print(f"{col_precios = }")
print(f"{col_existencias = }")

# Separamos los datos geográficos en latitud, longitud y una 
# lista con las claves
lat, lng, *claves = datos_geo
print(f"{lat=}")
print(f"{lng=}")
print(f"{claves=}")

# Invocamos la función desempaquetando manualmente
procesar_datos(datos_geo[0], datos_geo[1], datos_geo[2], 
                datos_geo[3], datos_geo[4])
# Invocamos la función desempaquetando automáticamente
procesar_datos(*datos_geo)

##############################################################################
# Desempaquetado de valores cuando una función retorna una tupla o lista




