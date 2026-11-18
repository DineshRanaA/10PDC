# 1. INTEGER (int)
age = 25

# 2. STRING (str)
name = "Dinesh"

# 3. LIST (list)
employees = ["Dinesh", "Arun", "Kumar"]  # Stores multiple values
employees.append("Raj")  # Adds a new employee at the end
print(employees)         # Prints the updated list

# 4. DICTIONARY (dict)
employee = {
    "name": "Dinesh",    # Key = name, Value = Dinesh
    "age": 25       # Key = age, Value = 25
}
employee["salary"] = 50000  # Adds a new key-value pair
employee["age"] = 26         # Updates the age value
print(employee)      # Prints updated

# 5. TUPLE (tuple)
departments = ("HR", "IT", "Sales", "Marketing")  # Creates a tuple

print(departments)       # Prints the complete tuple
print(departments[0])    # Gets the first element