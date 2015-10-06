# This program takes a number and runs the Collatz Sequence

# Defines a function that applies the Collatz Sequence calculation to a number
def collatz(number):
    if number % 2 == 0:
        collatzGood = number // 2
        print(collatzGood)
        return collatzGood
    else:
        collatzBad = 3 * number + 1
        print(collatzBad)
        return collatzBad

# Takes a number as input and loops the Collatz function until the value is equal to 1
userNum = input("Please write a number you want to do the Collatz Sequence with\n> ")
while True: 
    try:            # Making sure the value the user inputs is actually an integer
        userNum = int(userNum)
    except ValueError:
        print("Collatz Sequence is only possible with numbers...")
        break
    if userNum != 1:
        userNum = collatz(userNum)
    else:
        break
