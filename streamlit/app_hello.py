import streamlit as st 

number = st.number_input("Enter a number:")

if (st.button('Calculate Square')):
    st.text(f'Hello World! {number ** 2}')