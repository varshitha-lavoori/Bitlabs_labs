# Calculating the percentage of salary we used for bills
def bills():
    salary=int(input("Enter your current salary"))
    bill1=int(input("Enter the 1st bill u spent"))
    bill2=int(input("Enter the 2nd bill u spent"))
    bill3=int(input("Enter the 3rd bill u spent"))
    total=(bill1+bill2+bill3)
    percent=(total/salary)*100
    print(percent,"%")
bills()
