sheepsize = [5, 7 , 300, 90, 24, 50, 75]
total_size = 0
print ("Hello, my name is Nhung and these are my sheep sizes:")
print (*sheepsize, sep = ", ")
month = int (input("How many month you want to calculate the sheep flock? "))

for m in range (month):
    sheepmax = max(sheepsize)
    print ("MONTH {0}".format(m+1))
    
    # print biggest size
    print ("Now my biggest sheep has size {0}. Lets shear it!".format(sheepmax))
    
    #print flock size after shearing
    i = sheepsize.index(sheepmax)
    update_sheepmax = 8
    sheepsize[i] = update_sheepmax
    print("After shearing, this is my flock: {0}".format(*sheepsize, sep = ", ")) 

    #print one month later size
    for j in range (0,7):
        sheepsize[j] += 50
    print ("One month has passed, now here is my sheep flock size: {0}". format(*sheepsize, sep = ", "))

# print flock size in total:
for n in range (7):
    cal_size = int(sheepsize[n])
    total_size += cal_size
print("My flock has size in total: {0}".format(total_size))

#print money:
print("I would get: {0} * 2$ = {1}$".format(total_size, total_size*2))

