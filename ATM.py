def showbalance():
    print("your balance is ",balance)

def deposit():
    amount=float(input("you amount is "))
    if amount<=0:
        print("you dont have a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount=int(input("you amount is "))
    if amount>balance:
        print("insufficient money")
        return 0
    elif  amount<0:
        print("invalid amount")
        return 0
    else:
        return amount

balance=0
run= True

while run:
    print("Banking program")
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    choice=input("hey customer enter your choice(1-4):")

    if choice=='1':
        showbalance()
    elif choice=='2':
        balance += deposit()
    elif choice=='3':
        balance-=withdraw()
    elif choice =='4':
        run= False
    else:
        print("this number is not valid")
