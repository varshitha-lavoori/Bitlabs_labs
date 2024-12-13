
def grades():
    a=int(input("enter marks"))
    if(a>=91 and a<=100):
        print("The grade u recieved is S")
    elif(a>=81 and a<=90):
        print("The grade u recieved is A+")
    elif(a>=71 and a<=80):
        print("The grade u recieved is A")
    elif(a>=61 and a<=70):
        print("The grade u recieved is B+")
    elif(a>=51 and a<=60):
        print("The grade u recieved is B")
    elif(a>=41 and a<=50):
        print("The grade u recieved is C+")
    else:
        print("The person is failed")
grades()
