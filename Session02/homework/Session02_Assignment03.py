from turtle import *

shape("turtle")
speed(-1)

for i in range (3,7):
    for j in range(i):
        if i%2 == 1:
            color("blue")
        else:
            color("pink")
        left(360/i)
        forward(100)

    



mainloop ()