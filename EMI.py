import streamlit as st

# Title
st.title("💰 EMI Calculator")

# User Inputs
p = st.number_input("🏦 Enter the loan amount (Principal ₹):", min_value=0.0, step=1000.0, format="%.2f")
A = st.number_input("📈 Enter the annual interest rate (%):", min_value=0.0, step=0.1, format="%.2f")
n = st.number_input("📆 Enter the number of monthly installments:", min_value=1, step=1)

# Calculate EMI only if valid input
if st.button("Calculate EMI"):
    if A > 0 and n > 0:
        r = A / (12 * 100)  # monthly interest rate
        EMI = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    else:
        EMI = 0.0

    st.markdown("---")
    st.success(f"💸 Your Monthly EMI is: ₹ {EMI:,.2f}")

    total_payment = EMI * n
    total_interest = total_payment - p

    st.markdown(f"**📊 Total Payment:** ₹ {total_payment:,.2f}")
    st.markdown(f"**💼 Total Interest Payable:** ₹ {total_interest:,.2f}")
