# Implementa tu solución aquí

def residuo_2_con_7(n:int):
    if n < 0:
        raise ValueError("n menor que cero")
    
    return set(range(2, n + 1, 7))