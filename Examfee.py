import streamlit as st
from datetime import date

# Constants
REGULAR_FEE = 500
REGULAR_SUBJECT_FEE = 100  
SUPPLY_SUBJECT_FEE = 300
LATE_FEE = 100
DEADLINE_DATE = date(2025, 4, 30)

# App Title
st.title("📝 Exam Fee Payment Portal")
st.markdown("Welcome! Please choose your exam type and fill in the necessary details below.")

# Input: Exam Type
exam_type = st.radio("🎓 Select Exam Type:", ["Regular", "Supply"])

# Input: Today's Date
selected_date = st.date_input("📅 Select today's date", value=date.today())

# Subject Options
subject_options = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]

# Fee Calculation
total_fee = 0

if exam_type == "Regular":
    st.subheader("📚 Regular Exam Details")
    st.markdown(f"✅ Base Exam Fee: **₹{REGULAR_FEE}**")
    st.markdown("Each subject is assumed at ₹100 (for reference).")
    for subject in subject_options:
        st.markdown(f"- {subject}: ₹{REGULAR_SUBJECT_FEE}")
    total_fee = REGULAR_FEE

else:  # Supply Exam
    st.subheader("🛠️ Supply Exam Details")
    selected_subjects = st.multiselect("Select subjects for supply exam:", subject_options)

    subject_fee = len(selected_subjects) * SUPPLY_SUBJECT_FEE
    total_fee = subject_fee

    if selected_date > DEADLINE_DATE:
        st.warning(f"⚠️ Deadline exceeded! Late fee of ₹{LATE_FEE} will be added.")
        total_fee += LATE_FEE
    else:
        st.info("✅ Fee submitted before deadline. No late fee.")

# Submit Button
if st.button("💳 Submit & Calculate Fee"):
    if exam_type == "Supply" and not selected_subjects:
        st.error("❌ Please select at least one subject for the supply exam.")
    else:
        st.markdown("---")
        st.subheader("🧾 Fee Summary")

        if exam_type == "Supply":
            st.write("**Selected Subjects:**")
            for subject in selected_subjects:
                st.markdown(f"- {subject}: ₹{SUPPLY_SUBJECT_FEE}")
            st.markdown(f"**Subject Fee:** ₹{subject_fee}")

            if selected_date > DEADLINE_DATE:
                st.markdown(f"**Late Fee:** ₹{LATE_FEE}")

        st.success(f"✅ **Total Fee to be Paid: ₹{total_fee}**")
