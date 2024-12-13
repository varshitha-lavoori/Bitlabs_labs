
import streamlit as st
st.title("Gross Salary Calculation using streamlit")
basic_sal = st.number_input("Enter your basic salary:",min_value=0,step=1)
if st.button('Calculate gross salary'):
    hra = 0
    da = 0
    if (basic_sal < 10000):
        hra = basic_sal * (67 / 100)
        da = basic_sal * (73 / 100)
    elif (basic_sal >= 10000 and basic_sal <= 20000):
        hra = basic_sal * (69 / 100)
        da = basic_sal * (76 / 100)
    else:
        hra = basic_sal * (73 / 100)
        da = basic_sal * (89 / 100)
    gs = hra + da + basic_sal
    st.write(gs)
