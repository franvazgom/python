
def main():
    nombres = ['Laura', 'Pedro', 'Alicia', 'Fernando', 'Fernanda'] 
    nombres.append('Francisco')    
    nombres.append('Julia')    
    print(nombres)
    nombres.insert(1,'Juan')
    print(nombres)
    nombres.insert(1,'José')
    print(nombres)
    print('------------------')
    nombres.sort()
    print(nombres)
    nombres.reverse()
    print(nombres)
if __name__ == '__main__': 
    main()