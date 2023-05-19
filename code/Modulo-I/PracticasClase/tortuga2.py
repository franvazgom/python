import turtle

def main():
    t = turtle.Turtle()
    t.pensize(1)
    t.pencolor('red')
    t.speed(20)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-100, 200)
    t.pencolor('blue')
    t.pendown()
    t.forward(200)
    
    # for i in range(364):
    #     t.forward(300)
    #     t.right(91)
    

    input()
if __name__ == '__main__':
    main()