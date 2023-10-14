from turtle import *
  # Developer Mohammed Razin Cr
def fleur():
    for i in range(300):
        speed(40)
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(36)
fleur()
mainloop()