def main():
    nombre = input("Teclea tu nombre: ")
    # i = 0
    # while i < 5:
    #     print(f'{nombre} -> {i}')
    #     i += 1

    for i in range(5):
        print(f'{nombre} -> {i}')
    print("----------------")
    for i in range(1, 5):
        print(f'{i}' , end=' ')
    print()
    print("----------------")
    for i in range(1, 10, 2):
        print(f'{i}', end=' ')
    print()
    print("----------------")
    for i in range(0, 20, 5):
        print(f'{i}', end=' ')
    print()
    print("----------------")
    for i in range(5, 0, -1):
        print(f'{i}', end=' ')
    print()

if __name__ == '__main__':
    main()