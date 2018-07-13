num_month = int(input("How many month you want to calculate number of rabbit?  "))

dict_rabbit = {
    0: 1,
    1: 2,
}

list_rabbit = []

# sum_rabbit = 0

for i in range (2, num_month+1):
    sum_rabbit = (dict_rabbit[i-2] + dict_rabbit[i-1])
    dict_rabbit[i] = sum_rabbit

for key, value in dict_rabbit.items():
    print("Month {0}: {1} pair(s) of rabbit".format(key,value))