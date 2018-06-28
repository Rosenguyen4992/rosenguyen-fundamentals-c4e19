# print("Hello, this is a random number from 1 to 100: ")
# from random import randint
# n = randint(0, 100)
# if n < 30:
#     print("Hi there, my name is Ms Moody. I feel sad :<")
# elif n <60:
#     print("Hi there, my name is Ms Moody. I feel normal .__.")
# else:
#     print("Hi there, my name is Ms Moody. I feel awesome :D")

# dai = int(input("Bạn muốn vẽ hình rộng b"))



# for i in range (5):
#     for j in range (4):
#         print ("* ", end=" ")
#     # print()


# ve tam giac vuong nguoc:
# for j in range (1, 5):
#         print (" "*(5-j), "*"*j)
#         print()


for i in range(n):
    for j in range (n):
        if (j < n - i - 1):
            print(" ", end="")
        else:
            print("* ", end="")