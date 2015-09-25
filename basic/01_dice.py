# This is a basic dice rolling program. In the future I'll try to rewrite it
# in order to allow more complex rolls, for ex. 3d8+5 

import random

while True:
    print("Roll your die:")
    roll = input("> ")

    if roll in ("quit", "exit"):
        break

    elif roll in ("d4", "d6", "d8", "d10", "d12", "d20", "d100"):
        rolled = int(roll[1:])
        rolled = random.randint(1, rolled)
        print("You rolled a " + roll + " and it landed on: " + str(rolled))

    else:
        print("This is not a real die! try again with d4, d6, d8, d10, d12, d20 or d100")
