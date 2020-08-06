import turtle
import math

side = 20
num_sides = 3
turtle.shape('turtle')


def regular_polygons(num_sides):
    """
    Функция предназначена для построения правильных многоугольников.
    Принимает один парамер - число сторон.
    :param num_sides:
    :return:
    """
    deg = (num_sides - 2) * 180 / num_sides
    R = side/(2 * math.sin(math.pi / num_sides))
    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()
    turtle.left(180 - deg/2)
    while num_sides != 0:
        turtle.forward(side)
        turtle.left(180 - deg)
        num_sides -= 1
    turtle.right(180 - deg/2)


while num_sides != 11:
    regular_polygons(num_sides)
    side += 15
    num_sides += 1


