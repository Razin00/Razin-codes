import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor("black")
turtle.speed(0)
col=('white','red','orange','yellow','green','blue')
for i in range (360):
    turtle.pencolor(col[i%6])
    turtle.width(i/5+1)
    turtle.forward((i))
    turtle.left(40)