import turtle

turtle.setup(960, 720)

def circ(x):
    if x > 200:
        return
    turtle.circle(x, steps=100)
    turtle.left(5)
    print(x)
    circ(x + 1)

turtle.tracer(5, 0)
turtle.shape("triangle")
turtle.shapesize(1, 1, 1.5)
turtle.pencolor('black')
turtle.fillcolor('red')
turtle.begin_fill()
circ(1)
turtle.end_fill()
turtle.mainloop()
