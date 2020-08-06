import turtle

turtle.shape('turtle')
flowers = 3


def flower():
    """
    Функция рисует две симметричные окружности
    :return:
    """
    sides = 0
    while sides != 360:
        if sides <= 180:
            turtle.forward(3)
            turtle.left(2)
        elif sides > 180:
            turtle.forward(3)
            turtle.right(2)
        sides += 1


while flowers != 0:
    flower()
    turtle.left(60)
    flowers -= 1