# Implementa tu solución aquí

def multiplos_de_3(n:int):
    if n < 0:
        raise ValueError("n menor que 0")
    return set(range(0, n + 1, 3))
#


if __name__ == "__main__":
    ...


