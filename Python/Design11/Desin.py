import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('aqua')
def drewcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-6
def drawdesign():
    for i in range (10):
        drewcircle(140)
        turtle.right(36)
drawdesign()
turtle.done()