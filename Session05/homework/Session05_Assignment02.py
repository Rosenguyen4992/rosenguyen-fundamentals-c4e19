number = [1, 4, 8, 9, 0, 4, 3, 9, 7, 0, 2, 2, 4]

loop = True
#Cach 1: without Count () function
# count = 0
# while loop:
#     check_number = int(input("Which number do you want to count? "))
#     for i, item in enumerate (number):
#         if  item ==  check_number:
#             count += 1   
#     print ("{0} appear {1} time(s) in the list".format(check_number,count))
#     count = 0

# Cach 2: with count() function
while loop:
    check_number = int(input("Which number do you want to count? "))
    no_of_number = number.count(check_number)
    print ("{0} appear {1} time(s) in the list".format(check_number,no_of_number))


