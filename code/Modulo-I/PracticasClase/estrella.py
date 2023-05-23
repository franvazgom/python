import turtle

def main():
    t = turtle.Turtle()
    t.pensize(0.5)
    t.pencolor('red')
    t.speed(50)
    t.penup()
    tam_cuadrante = 400
    n = 50
    espacio = tam_cuadrante // n 
    # se dibuja el eje x y eje y
    t.goto(-tam_cuadrante, 0) 
    t.pendown()
    t.goto(tam_cuadrante,0)
    t.penup()
    t.goto(0, tam_cuadrante) 
    t.pendown()
    t.goto(0, -tam_cuadrante) 
    t.penup()
    #Se empieza con el primer cuadrante
    j = n
    t.speed(50)
    t.color("black")
    for i in range(1, n+1):
        t.goto(i * espacio , 0)
        t.pendown()
        t.goto(0 , j * espacio)
        t.goto(-i * espacio , 0)
        t.goto(0 , -j * espacio)
        t.goto(i * espacio, 0)
        t.penup()
        j -= 1

    input()
if __name__ == '__main__':
    main()