import streamlit as st
string = "Find if the number is even or odd"
st.set_page_config(page_title=string)

st.title('Find Odd-Even ')
x = st.number_input('Enter a number')
if (x).is_integer():
    if x%2==0:
      st.header("the number is even")
    elif x%2!=0:
      st.header("the number is odd")
else:st.subheader("please enter an integer")
