# Implementa tu solución aquí
import pdb

def multiplos_de_5(a:int, b:int):
    if a <= 0:
        raise ValueError("a es menor que 1")
    if b < a:
        raise ValueError("b es menor que a")
    
    falta_para_multiplo = (5 - (a % 5)) % 5
    return set(range(a + falta_para_multiplo, b + 1, 5))

