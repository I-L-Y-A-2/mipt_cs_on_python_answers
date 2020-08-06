import turtle

turtle.shape('turtle')
num_lines = 12

while num_lines != 0:
    turtle.right(30)
    turtle.forward(50)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
    num_lines -= 1