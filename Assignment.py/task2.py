# ask user for their fullname
user = input("Enter Your Full Name: ")
# convert fullname to uppercase
user.upper()
# convert fullname to lowercase
user.lower()

# display output
print("Full Name:", user)
print("Uppercase:", user.upper())
print("Lowercase:", user.lower())
# replace that with "_"
print("Modified:", '_'.join(user.split(" ")))
# display the length of character
print("Character:", len(user))
