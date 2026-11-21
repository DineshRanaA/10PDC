
# ==========================================
# STUDENT GRADE MANAGER
# Using Python and Streamlit
# ==========================================

import streamlit as st
import pandas as pd


# Step 1: Configure Streamlit page

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# Step 2: Define grading function

def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "F"


# Step 3: Initialize session state

# Streamlit reruns the complete script
# whenever a user interacts with the page.

# session_state preserves data between reruns.

if "students" not in st.session_state:

    st.session_state.students = []


# Step 4: Page title

st.title("🎓 Student Grade Manager")

st.write("Add students and manage their grades.")


# Step 5: Create student form

st.subheader("Add New Student")

with st.form("add_student_form"):

    name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )

    mark = st.number_input(
        "Student Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submit = st.form_submit_button("Add Student")


    # Step 6: Process form submission

    if submit:

        if not name.strip():

            st.error("Please enter student name.")

        else:

            student = {
                "name": name.strip(),
                "mark": mark,
                "grade": get_grade(mark)
            }

            # Store student in session state
            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# Step 7: Display student records

st.divider()

st.subheader("Student Results")


if st.session_state.students:

    # Convert student list into DataFrame
    df = pd.DataFrame(st.session_state.students)

    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # Step 8: Calculate class statistics

    marks = [
        student["mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)


    # Step 9: Display class metrics

    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Class Average",
        f"{average:.2f}"
    )

    col2.metric(
        "Highest Mark",
        highest
    )

    col3.metric(
        "Lowest Mark",
        lowest
    )


else:

    st.info("No students added yet. Add your first student!")


# Step 10: Display total student count

st.divider()

st.write(
    f"Total Students: {len(st.session_state.students)}"
)


# Step 11: Clear all student records

if st.session_state.students:

    if st.button("Clear All Students"):

        st.session_state.students = []

        st.rerun()
