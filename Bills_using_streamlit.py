import streamlit as st
st.title("Bills using streamlit")
salary = st.number_input("Enter your current salary")
bill1 = st.number_input("enter the 1st bill u spent")
bill2 = st.number_input("enter the 2nd bill u spent")
bill3 = st.number_input("enter the 3rd bill u spent")
total = (bill1 + bill2 + bill3)
if st.button("Calculate the salary u spents "):
    percent = (total / salary) * 100 if salary>0 else 0
    st.write(f'percentage is :{percent}%')
