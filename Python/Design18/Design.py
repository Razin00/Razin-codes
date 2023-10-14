import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(400)
for i in range(400):
    for color in ["red","white"]:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(60)
        squary.right(200)