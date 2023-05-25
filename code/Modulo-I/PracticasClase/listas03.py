import random

def main():
    nombres = ['Laura', 'Pedro', 'Alicia', 'Fernando', 'Fernanda'] 
    # print(random.choice(nombres))  
    nombres.sort()
    print(nombres)
    random.shuffle(nombres)
    print(nombres)


if __name__ == '__main__': 
    main()