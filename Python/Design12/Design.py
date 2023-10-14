import turtle
  # Developer Mohammed Razin Cr
turtle.bgcolor("black")
turtle.speed(0)
col=('white','red','white','red','white','red')
for i in range (560):
    turtle.pencolor(col[i%6])
    turtle.width(i/5+1)
    turtle.forward((i))
    turtle.left(200)