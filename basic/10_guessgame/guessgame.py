# This game will make you guess a number 
# and will try to help you succeed

import random

print("Hello, sir. May I know your name?")
name = input("> ")
print("Well, " + name + ", I'm thinking of a number between 1 and 20. Try to guess it!")

secretNum = random.randint(1, 20)
for guessesTaken in range(1, 6):
    try:
        guessedNum = int(input("> "))
    except ValueError:
        print("Please type a number...")
        continue
    if guessedNum != secretNum and guessesTaken == 5:
        print("Sorry... Better luck next time!")
    elif guessedNum == secretNum and guessesTaken == 1:
        print("That's right, and it only took you " + str(guessesTaken) + " try to guess!")
        break
    elif guessedNum == secretNum:
        print("That's right, and it only took you " + str(guessesTaken) + " tries to guess!")
        break        
    elif guessedNum > secretNum:
        print("Nope, too high!")
    else:
        print("Nope, too low!")