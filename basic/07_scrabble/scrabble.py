import sys

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

dictionary = []
filename = open("sowpods.txt", "r")
for word in filename:
    cleanword = word.strip()
    lowercleanword = str.lower(cleanword)
    dictionary.append(lowercleanword)
filename.close()

print("Welcome to the Scrabble cheater!")
print("This program contains " + str(len(dictionary)) + " valid Scrabble words")

