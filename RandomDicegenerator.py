import random
while True:
    print("1.roll dice")
    list=int(input("hey user input start number"))
    if list==1:
        number= random.randint(1,6)
        print (number)
    else:
        print("stop")
        break
