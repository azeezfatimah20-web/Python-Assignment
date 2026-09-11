# create a function to calculate length and width
def calculate_area(length, width):
    return length * width


# accepting input from user in a floating point
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
# calculate the area of a rectangle
area = calculate_area(length, width)
# display the output
print("The area of a rectangle is:", area)
