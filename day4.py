# 1. DICTIONARY -> FOR LOOP -> CONDITION
employee = {
    "name": "Dinesh",
    "age": 25
}

for key, value in employee.items():
    print(key, value)

# 2. TWO LISTS -> DICTIONARY -> FOR LOOP
names = ["Dinesh", "Arun", "Kumar", "Raj"]
salaries = [50000, 30000, 70000, 20000]

# Create empty dictionary
employees = {}

# Loop through both lists using zip()
for name, salary in zip(names, salaries):
    employees[name] = salary  # Add name and salary to dictionary

print("\nEmployee Dictionary:", employees)

# Loop through dictionary key and value
for name, salary in employees.items():
    print(name, salary)