n = int(input("Vui lòng nhập font size mong muốn:"))

rong = 19*n

cao = 5*n

# for i in range (1, cao+1):
#     if i == 1 or i == 5*n:
for j in range (1, rong+1):
            if j == 5*n or j == 10*n or j == 15*n or j == 14*n:
                print (" "*n, end = "")
            else:
                print ("*", end = "")
print()
    # elif i == 3*n:
    #     for l in range (1, rong+1):
    #         if l == 1 or l == (6*n) or l == (9*n) or l == (11*n) or l == (14*n) or l == (16*n) or l == (17*n) or l == (18*n) or l == (19*n):
    #             print ("* ", end = "")
    #         elif l%5 == 0 and l != (15*n):
    #             print (" ", end = "")
    #         elif l != (15*n):
    #             print (" ", end = "")
    #     print()
    # else:
    #     for k in range (1, rong+1):
    #         if k == 1 or k == (6*n) or k == (9*n) or k == (11*n) or k == (14*n) or k == (16*n):
    #             print ("* ", end = "")
    #         elif k%5 == 0 and k != (15*n):
    #             print (" ", end = "")
    #         elif k != (15*n):
    #             print (" ", end = "")
    #     print()



