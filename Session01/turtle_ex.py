from turtle import *

shape("turtle")
color("blue")
speed(-1)


# for i in range(4):
#     #draw a square
#     forward(100)
#     left(90)
    # forward(100)
    # left(90)
    # forward(100)
    # left(90)
    # forward(100)
    # left(13)

canh = int(input("Bạn muốn vẽ mấy cạnh?"))
for i in range (canh):
    forward(40)
    left(360/canh)


mainloop ()