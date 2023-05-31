import random

def imprime_diagonal(M):
    pass

def imprime_matriz2(M):
    filas = len(M)
    columnas = len(M[0])
    print()
    for i in range(filas):
        print('[\t', end='')
        for j in range(columnas):    
            print(f'{M[i][j]} \t', end='')
        print(']') #Enter

def imprime_matriz(M):
    for fila in M:
        print(fila)

def suma_matrices(M1, M2):
    filas = len(M1)
    columnas = len(M1[0])
    R = inicializa_matriz_0(filas, columnas)

    for fil in range(filas):
        for col in range(columnas):
            R[fil][col] = M1[fil][col] + M2[fil][col]
    
    return R

def llena_matriz(filas, columnas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columnas):
            F.append(int(input(f"M[{k},{i}]: ")))
        M.append(F)
    return M

def inicializa_matriz_random(filas, columnas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columnas):
            F.append(random.randint(1,100))
        M.append(F)
    return M

def inicializa_matriz_0(filas, columnas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columnas):
            F.append(0)
        M.append(F)
    return M

def main():
    M1 = inicializa_matriz_random(2,2)
    M2 = inicializa_matriz_random(2,2)
    print("Matriz 1:")
    imprime_matriz2(M1)
    print("Matriz 2:")
    imprime_matriz2(M2)
    M3 = suma_matrices(M1, M2)
    print("Matriz Resultado:")
    imprime_matriz2(M3)

if __name__ == '__main__': 
    main()