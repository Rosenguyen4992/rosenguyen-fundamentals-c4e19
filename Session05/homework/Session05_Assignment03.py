initial_bac = int(input("How many B bacterias are there? "))
time_bac = int(input("How much time in minutes will we wait? "))
if time_bac%2 == 0:
    print("After {0} minutes we would have {1} bacterias".format(time_bac,time_bac*initial_bac))
else:
    print("After {0} minutes we would have {1} bacterias".format(time_bac,(time_bac-1)*initial_bac))