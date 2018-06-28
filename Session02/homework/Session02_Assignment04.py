print("Hello!")
height = float(input("Please input your height in cm here:"))
weight = float(input("Please input your weight in kg here:"))
bmi = weight/(height/100)**2

if bmi < 16:
    print ("You are Severely underweight >__<")
elif bmi < 18.5:
    print ("You are Underweight:(")
elif bmi < 25:
    print ("You are normal :)")
elif bmi < 30:
    print ("You are overweight :(")
else:
    print ("You are obese >___<")
