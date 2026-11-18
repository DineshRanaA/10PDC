# 1. Employee details
name = "Dinesh"                  # Employee name
age = 25                         # Employee age
salary = 50000                   # Employee salary
experience = 3                   # Years of experience
is_active = True                 # Account status
role = "Admin"                   # Employee role

# IF condition
if age >= 18:               # Check age
    print("Eligible")       # If condition is True

# IF - ELIF - ELSE
if salary >= 100000:        # Check high salary
    print("High Salary")
elif salary >= 50000:       # Check medium salary
    print("Medium Salary")
else:
    print("Low Salary")     # If all conditions are False

# NESTED IF condition
if is_active:               # Check account status
    print("Account Active")
    if age >= 18:           # Check age inside IF
        print("Age Verified")
        if experience >= 2: # Check experience inside IF
            print("Promotion Eligible")
        else:
            print("Need More Experience")
    else:
        print("Age Not Eligible")
else:
    print("Account Inactive")

# 6. TERNARY OPERATOR
status = "Active" if is_active else "Inactive"
print("Status:", status)         # Prints ternary result

# 7. NESTED TERNARY
grade = "A" if salary >= 100000 else "B" if salary >= 50000 else "C"
print("Salary Grade:", grade)

# 8. ROLE-BASED ACCESS
if role == "Admin":              # Check admin role
    print("Full Access")
elif role == "Manager":          # Check manager role
    print("Manager Access")
else:
    print("Employee Access")     # Default access