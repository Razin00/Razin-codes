import turtle
  # Developer Mohammed Razin Cr
colors = ['blue','blue','yellow','blue','blue','blue','blue']
t = turtle.Pen()
t.speed(40)
t.pensize(0.1)
turtle.bgcolor('black')
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)