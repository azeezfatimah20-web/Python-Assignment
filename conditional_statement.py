# if-else statement

# a = input("Enter your name: ").strip()

# if a == "Fatimah":
#     print("Hello Fatimah")
#     if "o" in a:
#         print("True")
#     else:
#         print("False")

# else:
#     print("Hello Guest")
# print("How are you doing!")


# if-elif-else

# b = input("Enter your favourite color: ")
# if b == "blue":
#     print("you are enthusiastic")
# elif b == "green":
#     print("you are close to nature")
# elif b == "red":
#     print("you are and full of nature")
# else:
#     print(f"Hello energy {b}")


# # program to find biggest of two given numbers
# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))

# if n1 > n2:
#     print("Biggest Number is:", n1)
# else:
#     print("Biggest Number is:", n2)


# program to take a single digit number from the keyboard and print is value in English word.
n = int(input("Enter a digit from 0 to 9:"))
if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
else:
    print("PLEASE A DIGIT FROM 0 TO 9")

exampleOfFormattedStrings = 'My name is {name} and i am {age} years old, i love to watch movies on {movieName} station, i also love to sleep and shut people out {exp}.'

output = exampleOfFormattedStrings.format(
    name='Fatimah', age='12', movieName='Netflix', exp='sometimes')

print(output)
