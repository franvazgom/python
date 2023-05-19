def main():
    for i in range(50):
        if i % 3 == 0:
            continue
        print(f'i = {i}')
        if i > 10:
            break

if __name__ == '__main__':
    main()