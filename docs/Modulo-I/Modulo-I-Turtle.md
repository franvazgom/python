
```python
import turtle

def main():
    t = turtle.Turtle()

    t.pensize(0.5)
    t.pencolor("blue")
    t.speed(20)
    t.pendown()
    t.forward(200)
    t.right(91)
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(150)
    t.goto(-100,100)

    t.forward(300)
    input()

if __name__ == '__main__':
    main()
```