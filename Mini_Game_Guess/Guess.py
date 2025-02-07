# Create a guess game where the user has to guess a number and the computer tells them if they are too high or too low. until they guess the correct number

import random

num = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != num:
    if guess < num:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
    
print("You guessed it!")