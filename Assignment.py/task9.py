<<<<<<< HEAD
# Import the built-in random module
import random
# Generate a random number between 1 and 20.
number = random.randint(1, 20)
# Ask the user to guess the number.
guess = int(input("Guess a number between 1 and 20: "))
# Display: Too High, Too Low, or Correct.
if guess > number:
    print("Too High!")
elif guess < number:
    print("Too Low!")
else:
    print("Correct!")
=======
# import random

# number = random.randint(1, 20)

# guess = int(input("Guess a number between 1 and 20: "))

# if guess > number:
#     print("Too High!")
# elif guess < number:
#     print("Too Low!")
# else:
#     print("Correct!")


import random

number = random.randint(1, 20)

guess = int(input("Guess a number between 1 and 20: "))

if guess > number:
    print("Too High!")
elif guess < number:
    print("Too Low!")
else:
    print("correct!")
>>>>>>> a9cbbccd8e4de4f4a6ef51ec8b3a7e3591f3cfb8
