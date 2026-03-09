# Implementa tu solución aquí

def multiplos(k:int, n:int):
    if k <= 0:
        raise ValueError("k menor que 1")
    if n < 0:
        raise ValueError("n menor que cero")
    
    return set(range(0, n + 1, k))