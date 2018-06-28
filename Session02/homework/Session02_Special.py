n = int(input("Vui lòng nhập font size mong muốn:"))

rong = 19*n

cao = 5*n

for i in range (1, cao+1):
    if i == 1 or i == 5*n:
        for j in range (1, rong+1):
            if (4*n) < j <= (5*n) or (9*n) < j <= (10*n) or (13*n) < j < (15*n):
                print (" ", end = "")
            else:
                print ("*", end = "")
        print()
    elif i == 3*n:
        for m in range (1, rong+1):
            if 1 <= m <=n or (5*n) < m <= (6*n) or (8*n) < m <= (9*n)  or (10*n) < m <= (11*n) or (13*n) < m <= (14*n) or (15*n) <= m <= (19*n):
                print ("*", end = "")
            else:
                print (" ", end = "")
        print()
    else:
        for k in range (1, rong+1):
            if 1 <= k <=n or (5*n) < k <= (6*n) or (8*n) < k <= (9*n)  or (10*n) < k <= (11*n) or (13*n) < k <= (14*n) or (15*n) <= k < (16*n):
                print ("*", end = "")
            else:
                print (" ", end = "")
        print()



