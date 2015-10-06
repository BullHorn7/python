# Learning about handling exceptions.

print('How many cats do you have?')
numCats = input("> ")
try:
    if int(numCats) >= 3:
        print('That is a lot of cats')
    elif int(numCats) == 0:
        print("My condolences")
    elif int(numCats) < 0:
        print("That's not possible")
    else:    
        print("That's really not that many cats")
except ValueError:
    print("You didn't enter a number")