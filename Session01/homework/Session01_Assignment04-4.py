from turtle import *

shape("turtle")
color("blue")
speed(-1)
fillcolor("yellow")

begin_fill()
for i in range (6):
    circle(90, extent=None, steps=None)
    left(60)
end_fill()

mainloop ()