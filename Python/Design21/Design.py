import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor("black")                   
seven = turtle.Turtle()
seven.speed(40)
turtle.pensize(4)
def drawSquare():
    seven.forward(100)

    seven.forward(100)
    seven.right(90)
    seven.right(90)
    seven.fd(100)

    seven.fd(100)
    seven.rt(90)
    seven.rt(90)

for i in range(100):
    for colors in ["Yellow"]:
        seven.color(colors)
        drawSquare()
        seven.rt(4)