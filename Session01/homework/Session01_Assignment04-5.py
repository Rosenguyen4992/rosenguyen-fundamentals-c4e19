from turtle import *

shape("turtle")
color("blue")
speed(-1)
fillcolor("yellow")

begin_fill()
for i in range (60):
    circle(90, extent=None, steps=None)
    left(6)
end_fill()

mainloop ()