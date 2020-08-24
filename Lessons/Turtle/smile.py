import turtle as t

t.shape('turtle')


def circle(len_side):
    """
    Функция рисует круг. Параметр len принимает положительное число для определения длины окружности.
    """
    sides = 120
    while sides != 0:
        t.forward(len_side)
        t.left(3)
        sides -= 1


def spring(len_side):
    """
    Функция рисует дугу. Параметр len_side принимает число для определения длины дуги
    """
    sides = 0
    while sides != 60:
        t.forward(len_side)
        t.right(3)
        sides += 1


t.fillcolor('yellow')
t.begin_fill()
circle(5)
t.end_fill()

t.penup()
t.goto(-35, 125)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
circle(0.5)
t.end_fill()

t.penup()
t.goto(35, 125)
t.pendown()
t.begin_fill()
circle(0.5)
t.end_fill()


t.penup()
t.goto(0, 90)
t.right(90)
t.pendown()
t.color('black')
t.width(5)
t.forward(30)


t.penup()
t.goto(40, 75)
t.pendown()
t.color('red')
spring(2)