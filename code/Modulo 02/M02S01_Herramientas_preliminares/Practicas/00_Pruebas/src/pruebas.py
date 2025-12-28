
##############################################################################
# Trabajando con conjuntos

# Conjuntos
A = {1, 2, 3, 4, 8}
B = {3, 5, 23, 6, 7, 1}

# Pertenencia
1 in A
5 not in B
# Subconjunto
A <= B
A >= B
# Subconjunto propio
A < B
A > B
# Unión
A | B
# Intersección
A & B
# Diferencia
A - B
# Diferencia simétrica
A ^ B


##############################################################################


# Lista de números pares
a = [2 * i for i in range(10)]
# Conjunto de números impares
b = {2 * i + 1 for i in range(10)}
# Diccionario que mapea números a su doble
c = {i:2 * i for i in range(5)}
# Lista de listas vacías
d = [[] for _ in range(8)]
# Mas ejemplos
e = [k + v for k,v in c.items()]
f = [[i] * i for i in range(1, 10)]


##############################################################################


from datetime import datetime, timedelta

hoy = datetime.now()
#> datetime.datetime(2022, 5, 17, 20, 59, 42, 996482)
manana = hoy + timedelta(days=1)
#> datetime.datetime(2022, 5, 18, 21, 11, 40, 803855)
manana_fecha = manana.strftime("%d-%m-%Y")
#> '18-05-2022'
navidad = datetime.strptime("25/12/2022", "%d/%m/%Y")
#> datetime.datetime(2021, 12, 10, 0, 0)
dias_para_navidad = (navidad - hoy).days
#> 222


##############################################################################


from datetime import datetime

# Lista de números pares <= n
pares = lambda n: [i for i in range(0, n, 2)]
# Convertir fechas "dd/mm/aaaa" a datetime
dt = lambda f: datetime.strptime(f, "%d/%m/%Y")
# Calcular los días desde una fecha hasta otra,
# ambas en formato "dd/mm/aaaa".
dias_dif = lambda f1, f2: (dt(f2) - dt(f1)).days


##############################################################################


# Valor absoluto de un número
abs()
# Revisa si todos los valores son True
all()
# Revisa si algun valor es True
any()
# Revisa si un objeto parece invocable
callable()
# Borrar, obtener, verificar existencia
# y modificar un atributo de un objeto
delattr()
getattr()
hasattr()
setattr()
# Espacio de nombres de un objeto
dir()
# Enumerar un iterable
enumerate()
# Lee una linea de la entrada
input()
# Revisa si un objeto es instancia de 
# alguna de las clases especificadas
isinstance()
# Revisa si una clase es subclase de 
# alguna de las clases especificadas
issubclass()
# Máximo, mínimo y suma de un iterable
max()
min()
sum()
# Tipo de objeto
type()
# Unir horizontalmente dos o más iterables
zip()
# Aplicar funcion a elementos de iterable
map()
# Ordenar un iterable
sorted()


##############################################################################


# Indice fuera de rango
IndexError
# Llave de mapeo no válida
KeyError
# Cuando un método no está implementado
NotImplementedError
# Parámetro recibido no válido
ValueError
# El tipo de dato de un parámetro no es
# válido
TypeError


##############################################################################


nombre, edad, asegurado = ["Luis", 35, True]

def secuencia(inicio, fin, incremento):
    return list(range(inicio, fin, incremento))

parametros = [1, 10, 2]
secuencia(*parametros)
secuencia(*(2, 20, 4))


##############################################################################


def cobrar(monto:float, tarjeta:str) -> bool:
    ...


def total(cantidad:int, precio:int|float) -> float:
    ...

def descontar(  precios:list[float], 
                porcentaje:float|None
    ) -> list[float]:
    ...

def empaquetar( producto:str,
                cantidad:int
    ) -> dict[str, int]:
    ...
