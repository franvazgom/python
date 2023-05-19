import turtle

def main():
    t = turtle.Turtle()
    t.pensize(2)
    t.pencolor('red')
    t.speed(1)
    t.pendown()
    t.forward(200)
    t.right(90)
    t.pencolor('blue')
    t.forward(200)
    t.right(90)
    t.pencolor('red')
    t.forward(200)
    t.right(90)
    t.pencolor('green')
    t.forward(200)
    t.right(90)
    input()
if __name__ == '__main__':
    main()