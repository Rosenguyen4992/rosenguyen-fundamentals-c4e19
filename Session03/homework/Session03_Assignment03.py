from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

shape("turtle")
speed(-1)
color_code = 0

for i in range (3,8):
    for j in range(i):
        color(colors[color_code])
        left(360/i)
        forward(100)
    color_code += 1

mainloop()