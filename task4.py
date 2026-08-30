# print a multiplication table (1, 12) for a number entered by user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

for i in range(1, number1 + 1):
    for j in range(1, number2 + 1):

        print(f"{i} * {j} = {i*j}")
