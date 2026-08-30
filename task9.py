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
