'''
Este programa muestra las llamdas recursivas que son necesarias para ejecutar
la función fibonacci de manera recursiva. 
El objetivo es entender la recursividad y el uso excesivo de llamadas y memoria utilizada 
'''

constante = 1
num_llamadas = 0
def fibonacci_llamadas(n, ntabs):
    global num_llamadas
    num_llamadas += 1
    # print(n, ntabs)
    tabs = '\t'*(ntabs)
    if n > 1:
        print(tabs + f'Fibo({n}) -> Fibo({n-1}) + Fibo({n-2})')
    else:
        print(tabs + f'Fibo({n})')
    if n <= 1:
        print(tabs + f'Fibo({n}) fin, return {n}')
        return n
    else:
        res = fibonacci_llamadas(n-1, (constante - (n-1))) + fibonacci_llamadas(n-2, (constante - (n-1)))
        print(tabs + f'Fibo({n}) fin, return {res}')
        return res

def main():
    global constante
    n = int(input('N = '))
    constante  = n
    fibonacci_llamadas(n,0)
    print(f'\nNúmero de llamadas a la función Fibonacci: {num_llamadas}\n')

if __name__ == '__main__':
    main()