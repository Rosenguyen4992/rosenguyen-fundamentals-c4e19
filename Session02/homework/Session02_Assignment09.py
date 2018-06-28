n = int(input("Please input the number of 1's and 0's you want to print:"))

for i in range (1, n+1):
    if i%2 == 1:
        print ("1 ", end = "")
    else:
        print ("0 ", end = "")