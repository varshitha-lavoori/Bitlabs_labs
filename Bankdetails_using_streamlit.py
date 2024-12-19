import streamlit as st
st.title("Bank details using streamlit")

actual=st.number_input("enter actual amount:",key="actual_input")
amt=0
amt1=0
def bank_deposit_system():
    pin = "1234"
    max = 3
    for attempt in range(max):
        entered = st.text_input("Enter your password: ",key=f"{attempt}")
        if entered == pin:
            st.write("Password correct! Welcome to the bank deposit system.")
            break
        else:
            remaining_attempts = max - attempt - 1
            st.write(f"Incorrect password. You have {remaining_attempts} {'chance' if remaining_attempts ==1 else 'chances'} left.")
            if remaining_attempts ==0:
                st.write("You have entered the wrong password 3 times. Access denied.")
                break



    opt = int(st.number_input("choose an option:",step=1))
    match opt:
        case 1:
            deposit()
            #st.write("deposited")

        case 2:
            withdraw()
            #st.write("withdraw")
        case 3:
            bal_enquiry()
            #st.write("bal enquiry")
        case _:
            st.write("invalid option")

def deposit():
    global amt
    amt=st.number_input("enter amount to be deposited:")
    if st.button("calculate"):
        if amt%100==0:
            if amt>=100 and amt<=50000:
                st.write("deposited successfully")
                bal=actual+amt
                st.write("Balance is:",bal)
            else:
                st.write("entered amt shoul be btw 100 to 50k")
        else:
            st.write("entered amt shopuld be of multiples of 100")

def withdraw():
    global amt1
    amt1 = st.number_input("enter amount to be withdraw")
    if st.button("withdraw calculate"):
        if actual>=500:
            if amt1%100==0:
                if amt1 >=100 and amt1 <actual:
                    if amt1<=20000:
                        st.write("withdrawn successfully")
                        balance = actual - amt1
                        st.write(balance)
                    else:
                        st.write("transaction limit 20k")
                else:
                    st.write("entered amt should be btw 100 to 50k")
            else:
                st.write("entered amt shopuld be of multiples of 100")
        else:
            st.write("min balance 500")

def bal_enquiry():
    bal=actual+amt-amt1
    st.write(bal)

bank_deposit_system()





