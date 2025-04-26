#tip caluclator
import streamlit as st

bill = st.number_input("Enter the food item bill amount")

if bill <= 1000:
    tip = bill * 0.02  
elif bill <= 1500:     
    tip = bill * 0.05  
else:                 
    tip = bill * 0.10  

st.write(f"Tip amount is {tip:.2f}")  
st.write(f"Total to pay: {bill + tip:.2f}")"""

