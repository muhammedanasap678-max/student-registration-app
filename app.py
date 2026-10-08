import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Registration System",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Registration System")
st.write("Python CCE Project using Streamlit")

st.divider()

# Student details
st.header("👤 Student Details")

name = st.text_input("Full Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=15
)

student_class = st.selectbox(
    "Class",
    [
        "8th Standard",
        "9th Standard",
        "10th Standard",
        "11th Standard",
        "12th Standard"
    ]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

email = st.text_input("Email Address")

phone = st.text_input("Phone Number")

st.divider()

# Subject selection
st.header("📚 Subject Selection")

subjects = st.multiselect(
    "Choose your subjects",
    [
        "English",
        "Malayalam",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "History",
        "Computer Science"
    ]
)

st.divider()

# Registration
if st.button("📝 Register Student"):

    if name == "":
        st.warning("Please enter the student's name.")

    elif email == "":
        st.warning("Please enter the email address.")

    elif len(subjects) == 0:
        st.warning("Please select at least one subject.")

    else:
        st.success("✅ Student registered successfully!")

        st.subheader("📋 Registration Summary")

        st.write("**Name:**", name)
        st.write("**Age:**", age)
        st.write("**Class:**", student_class)
        st.write("**Gender:**", gender)
        st.write("**Email:**", email)
        st.write("**Phone:**", phone)
        st.write("**Subjects:**", ", ".join(subjects))

        # Age eligibility
        if age >= 18:
            st.info("🔵 The student is 18 or above.")
        else:
            st.info("🟢 The student is under 18.")

st.divider()

st.caption("Python CCE Project • Student Registration System")
