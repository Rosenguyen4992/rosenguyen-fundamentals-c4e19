sheepsize = [5, 7 , 300, 90, 24, 50, 75]

print ("Hello, my name is Nhung and these are my sheep sizes:")
print (*sheepsize, sep = ", ")
# print ("Now my biggest sheep has size {0}. Lets shear it!".format(sorted (sheepsize, reverse=True)[:1]))
print ("Now my biggest sheep has size {0}. Lets shear it!".format(max(sheepsize)))