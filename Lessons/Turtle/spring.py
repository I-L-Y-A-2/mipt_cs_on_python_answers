import turtle as t

t.shape('turtle')
t.left(90)
t.penup()
t.goto(-70, 0)
t.pendown()


def spring(len_side):
    """
    Функция рисует дугу. Параметр len_side принимает число для определения длины дуги
    """
    sides = 0
    while sides != 60:
        t.forward(len_side)
        t.right(3)
        sides += 1


spring_num = 0
while spring_num != 4:
    spring(3)
    spring(0.5)
    spring_num += 1