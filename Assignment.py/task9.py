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
