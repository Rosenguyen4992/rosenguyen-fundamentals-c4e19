n = int(input("Please input the number you want to print:"))

lenN = len(str(n))

for i in range (1, n+1):
    for j in range (1, n+1):
        m = str(i*j)
        lenM = len(m)
        print (i*j, " "*(lenN-lenM+1), end = "")
    print ()
