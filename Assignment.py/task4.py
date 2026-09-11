# print a multiplication table (1, 12) for a number entered by user
number = int(input("Enter the first number: "))

for i in range(1, number + 1):
    for j in range(1, 13):
        print(f'{i} times {j} = {i * j}')
