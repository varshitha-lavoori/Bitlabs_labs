# streamlit is used for creating web apps quickly
import streamlit as st
st.title("This is simple App")
#used to display the title on webpage

n1=st.number_input("Enter number",min_value=1,step=1)#number_input used to create an input box with the text enter number where the min value of that box is 1 and it increase or decrease by 1 value

st.text("This is my first webpage")
st.header("This is header with large size")
st.subheader("This is an text with smaller header")
st.markdown("**Bold Text varshii** and *Italic Text*")

#A versatile function that can display text, dataframes, and more. It automatically figures out how to display the data based on its type.
st.write("This is some text!")
st.write([1,
2, 3,
4, 5])
# Displays a list

if st.checkbox("Show text"):
    st.write("You checked the box!")
    choice = st.radio("Choose your favorite fruit", ("Apple","Banana", "Cherry"))
    st.write("You selected:", choice)

name = st.text_input('Enter your name')
st.write(f'Hello, {name}')

#for multiline inputs
comment = st.text_area('Leave a comment')
st.write(f'Your comment: {comment}')


number = st.number_input('Enter a number')
st.write(number)

st.code("import java.util.*; \n System.out.println('hello');")

#used to display images
from PIL import Image
img = Image.open('uses-of-python.jpg')
st.image(img)

#st.audio('filename'),st.video('filename')

#A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
#The data passed to the DataFrame() function is a dictionary, where:
#The keys A and B represent column names.
#The values [1, 2, 3] and [4, 5, 6] represent the column data

import pandas as pd
df = pd.DataFrame({'A': [1,
2,
3], 'B': [4,
5,
6]})
st.dataframe(df)
st.table(df)


#Creates a dropdown menu for selecting a single option.
option = st.selectbox('Choose an option', ['Option 1','Option 2'])
st.write(f'You selected {option}')

#age = st.slider('Select your age')
age = st.slider('Select your age',min_value=0,max_value=100)
st.write(f'Your age is {age}')


if st.button("Even/Odd"):
#used to create an button
    if n1%2==0:
        st.success("Even number")
    else:
        st.error("Odd number")
