
actual=int(input("enter actual amount:"))
amt=0
amt1=0
def bank_deposit_system():
    pin = "1234"
    max = 3
    for attempt in range(max):
        entered = input("Enter your password: ")
        if entered == pin:
            print("Password correct! Welcome to the bank deposit system.")
            break
        else:
            remaining_attempts = max - attempt - 1
            print(f"Incorrect password. You have {remaining_attempts} {'chance' if remaining_attempts ==1 else 'chances'} left.")
            if remaining_attempts ==0:
                print("You have entered the wrong password 3 times. Access denied.")
                break



    opt = int(input("choose an option:"))
    match opt:
        case 1:
            deposit()
            print("deposited")

        case 2:
            withdraw()
            print("withdraw")
        case 3:
            bal_enquiry()
            print("bal enquiry")
        case _:
            print("invalid option")

def deposit():
    global amt
    amt=int(input("enter amount to be deposited:"))
    if amt%100==0:
        if amt>=100 and amt<=50000:
            print("deposited successfully")
            bal=actual+amt
            print("Balance is:",bal)
        else:
            print("entered amt should be btw 100 to 50k")
    else:
        print("entered amt should be of multiples of 100")

def withdraw():
    global amt1
    amt1 = int(input("enter amount to be withdraw"))
    if actual>=500:
        if amt1%100==0:
            if amt1 >=100 and amt1 <actual:
                if amt1<=20000:
                    print("withdrawn successfully")
                    balance = actual - amt1
                    print(balance)
                else:
                    print("transaction limit 20k")
            else:
                print("entered amt should be btw 100 to 50k")
        else:
            print("entered amt should be of multiples of 100")
    else:
        print("min balance 500")

def bal_enquiry():
    bal=actual+amt-amt1
    print(bal)

bank_deposit_system()





