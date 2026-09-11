def calculate_area(length, width):
    return length * width


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = calculate_area(length, width)
print("The area of the rectangle is:", area)
