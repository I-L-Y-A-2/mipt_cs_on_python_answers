import turtle
import math


turtle.shape('turtle')


def flower(r):
    """
    Функция рисует две симметричные окружности
    :return:
    """
    c = 2 * math.pi * r
    len_side = c/180
    sides = 0
    while sides != 361:
        if sides <= 180:
            turtle.forward(len_side)
            turtle.left(2)
        elif sides > 180:
            turtle.forward(len_side)
            turtle.right(2)
        sides += 1


circles = 0
r = 20
turtle.left(90)
while circles != 10:
    flower(r)
    r += 10
    circles += 1