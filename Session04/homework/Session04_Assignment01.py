from turtle import *

color("blue")
speed(-1)

for j in range (18):
    for i in range (2):
        for k in range (2):
            forward(100)
            left (90)
        forward (100)
    left(15)

mainloop()