import turtle

turtle.shape('turtle')
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()

sides = 180
while sides != 0:
    turtle.forward(3)
    turtle.left(3)
    sides -= 1