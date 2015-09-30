import sys

# Square
amount = int(input("How big of a square would you like to see, nerd?\n--> "))
for number in range(amount):
    for value in range(amount):
        if number == 0 or value == 0 or number == amount-1 or value == amount-1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    print("")

# Triangle
amount = int(input("How big of a triangle would you like to see, nerd?\n--> "))
for number in range(amount):
    for value in range(number+1):
        print(value)
        if value == 0 or value == number or number+1 == amount:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    print("")