import random

num = random.randint(1, 10)
guess = 0

while guess != num:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")       
    else:
        print("Congratulations! You've guessed the number.")
