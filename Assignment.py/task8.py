<<<<<<< HEAD
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")

# Create and write to the file
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Department: " + department + "\n")

# Read and display the file
print("\nStudent Information:")
with open("student.txt", "r") as file:
    print(file.read())

# Get favourite language
language = input("Enter your favourite programming language: ")

# Append to the file
with open("student.txt", "a") as file:
    file.write("Favourite Language: " + language + "\n")

# Read and display updated file
print("\nUpdated Student Information:")
with open("student.txt", "r") as file:
    print(file.read())
=======
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")

# Create and write to the file
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Department: " + department + "\n")

# Read and display the file
print("\nStudent Information:")
with open("student.txt", "r") as file:
    print(file.read())

# Get favourite language
language = input("Enter your favourite programming language: ")

# Append to the file
with open("student.txt", "a") as file:
    file.write("Favourite Language: " + language + "\n")

# Read and display updated file
print("\nUpdated Student Information:")
with open("student.txt", "r") as file:
    print(file.read())
>>>>>>> a9cbbccd8e4de4f4a6ef51ec8b3a7e3591f3cfb8
