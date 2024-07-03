import random
import datetime
name = input("What is your name? ")
print("\nHello, " + name + "! " + "Welcome to the guessing game\nYour objective is to guess a number between 1 and 100\nTry to do it in the least number of guesses!\n")
num = random.randint(1, 100)
guesses = 0
while True:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1
        if guess < num:
            print("Too low! Guess Higher!\n")
        elif guess > num:
            print("Too high! Guess Lower!\n")
        else:
            print("Congratulations! You guessed the number in " + str(guesses) + " guesses!")
            with open("scores.csv", "a") as file:
                file.write(name + "," + str(guesses) + "," + str(datetime.datetime.now()) + "\n")
            break
    except ValueError:
        print("Please enter a valid number")
