# ask users for their grade
Grade = int(input('Enter Student Grade: '))
if Grade >= 70:
    print("Your Grade is A, Hurray!🥳")
elif Grade >= 60:
    print("Your Grade is B, Hurray!🥳")
elif Grade >= 50:
    print("Your Grade is C, Hurray!🥳")
elif Grade >= 45:
    print("Your Grade is D, Bad!🫩")
elif Grade >= 40:
    print("Your Grade is E, So Bad!🫩")
else:
    print("You Failed!😓")
