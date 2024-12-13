import streamlit as st
st.title("Finding grades using streamlit")
a=st.number_input("enter marks")
if st.button("Find grades"):
    if(a>=91 and a<=100):
        st.write("The grade u recieved is: S")
    elif(a>=81 and a<=90):
        st.write("The grade u recieved is: A+")
    elif(a>=71 and a<=80):
        st.write("The grade u recieved is: A")
    elif(a>=61 and a<=70):
        st.write("The grade u recieved is: B+")
    elif(a>=51 and a<=60):
        st.write("The grade u recieved is: B")
    elif(a>=41 and a<=50):
        st.write("The grade u recieved is: C+")
    else:
        st.write("The person is failed")

