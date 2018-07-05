from turtle import *

color("blue")
speed(-1)

for j in range (10, 166, 3):
    for k in range (4):
        forward (j)
        left (90)
    left (10)
    j += 1



mainloop()