sheepsize = [5, 7 , 300, 90, 24, 50, 75]
sheepmax = max(sheepsize)
print ("Hello, my name is Nhung and these are my sheep sizes:")
print (*sheepsize, sep = ", ")
print ("Now my biggest sheep has size {0}. Lets shear it!".format(sheepmax))
print("After shearing, this is my flock: ")

i = sheepsize.index(sheepmax)

update_sheepmax = 8
sheepsize[i] = update_sheepmax

print (*sheepsize, sep = ", ") 
