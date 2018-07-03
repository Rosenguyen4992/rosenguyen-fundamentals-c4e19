from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

shape("turtle")
speed(-1)
color_code = 0

for i in range (0,5):
    for j in range(2):
        color(colors[color_code])
        begin_fill()
        left(90)
        forward(200)
        left(90)
        forward(100)
        end_fill()
    forward(100)
    
    color_code += 1

mainloop()