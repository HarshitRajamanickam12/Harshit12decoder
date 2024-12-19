Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
bmi=Weight/(Height*Height)
print("your Body Mass Index is: ",bmi)

if(bmi<=16):
	print("you are severely underweight")
elif(bmi<=18.5):
	print("you are underweight")
elif(bmi<=25):
	print("you are Healthy")
elif(bmi<=30):
	print("you are overweight")
