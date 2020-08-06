import turtle

turtle.shape('turtle')
number_squares = 10
len_side = 25
a, b = 0, 0

while number_squares != 0:
    turtle.goto(a, b)
    turtle.pendown()
    for x in range(4):
        turtle.forward(len_side)
        turtle.left(90)
    number_squares -= 1
    len_side += 10
    a -= 5
    b -= 5
    turtle.penup()