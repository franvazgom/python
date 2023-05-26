

def llena_lista(n):
    datos = []
    for i in range(n):
        datos.append(input())
    return datos

def elimina_duplicados(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def main():
    num = int(input())
    original = llena_lista(num)
    res = elimina_duplicados(original)
    print(original)
    print(res)

if __name__ == '__main__': 
    main()