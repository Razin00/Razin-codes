import turtle
  # Developer Mohammed Razin Cr
t = turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while(True):
    for i in range(6):
        for colors in ("red","blue","pink","green"):
            turtle.color(colors)
            turtle.circle(100)
            turtle.forward(10)
            turtle.circle(100)
            turtle.left(10)

turtle.hideturtle()
turtle.mainloop()