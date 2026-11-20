
# ==========================================
# STUDENT GRADE MANAGER
# ==========================================


# Step 1: Create an empty list to store students

students = []

# We use a list of dictionaries.
# Each dictionary stores one student's name and mark.
# Duplicate student names are allowed.


# Step 2: Function to calculate student grade

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
        return "E"


# Explanation:
# get_grade(92) returns A
# get_grade(85) returns B
# get_grade(75) returns C
# get_grade(65) returns D
# get_grade(45) returns E


# Step 3: Function to add a student

def add_student():

    # Get student name from user
    name = input("Enter student name: ").strip()

    # Check whether name is empty
    if not name:
        print("Student name cannot be empty!")
        return

    try:

        # Get student mark and convert it to float
        mark = float(input("Enter student mark: "))

        # Validate mark range
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return

        # Create a dictionary for student details
        student = {
            "name": name,
            "mark": mark
        }

        # Add dictionary to students list
        students.append(student)

        print("Student added successfully!")

    except ValueError:

        # Handle invalid input like abc
        print("Please enter a valid number!")


# Explanation:
# input() gets information from the user.
# float() converts the mark into a number.
# try-except handles invalid number input.
# append() adds the student dictionary to the list.
# return exits the function when validation fails.


# Step 4: Function to display student results

def show_results():

    # Check whether students list is empty
    if not students:
        print("No student records available!")
        return

    # Display table heading
    print("\n" + "=" * 40)
    print(f"{'Name':<15} {'Mark':<10} {'Grade':<10}")
    print("=" * 40)

    # Create an empty list for marks
    marks = []

    # Loop through every student
    for student in students:

        # Get values from dictionary
        name = student["name"]
        mark = student["mark"]

        # Calculate grade
        grade = get_grade(mark)

        # Add mark to marks list
        marks.append(mark)

        # Display student details
        print(f"{name:<15} {mark:<10.1f} {grade:<10}")

    print("=" * 40)

    # Calculate class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display statistics
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest:.1f}")
    print(f"Lowest: {lowest:.1f}")

    print("=" * 40)


# Explanation:
# for student in students loops through every student.
# student["name"] gets the student's name.
# student["mark"] gets the student's mark.
# append() stores marks for calculations.
# sum() calculates total marks.
# len() calculates the number of students.
# max() finds the highest mark.
# min() finds the lowest mark.
# :.1f displays numbers with one decimal place.
# :<15 aligns text to the left in 15 spaces.


# Step 5: Main menu using while loop

while True:

    print("\n===== STUDENT GRADE MANAGER =====")

    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    # Get user menu choice
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")


# Explanation:
# while True runs the menu continuously.
# choice == "1" calls add_student().
# choice == "2" calls show_results().
# choice == "3" executes break and exits the loop.
# else handles invalid menu choices.