import turtle

def main():
    t = turtle.Turtle()
    t.pensize(0.5)
    t.pencolor('red')
    t.speed(50)
    t.pendown()
    
    for i in range(91):
        t.forward(300)
        t.right(91)
    
    t.penup()
    t.goto(-150,0)
    t.pendown()
    t.pencolor('blue')
    for i in range(91):
        t.forward(300)
        t.right(91)
    
    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.pencolor('red')
    for i in range(91):
        t.forward(300)
        t.right(91)
    

    input()
if __name__ == '__main__':
    main()