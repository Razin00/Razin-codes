import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(400)
for i in range(400):
    for color in ["chartreuse1","green"]:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(69)
        squary.right(200)