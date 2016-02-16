scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

word_list = []
filename = open("sowpods.txt", "r")
for word in filename:
    cleanword = word.strip().lower()
    word_list.append(cleanword)
filename.close()

print("\nWelcome to the Scrabble cheater!")
print("This program contains " + str(len(word_list)) + " valid Scrabble words")
print("Quit the program at any time by typing '.quit'")

def scrabble_cheat():
    valid_words = []
    for word in word_list:
        available_letters = rack[:]
        valid = True
        for letter in word:
            if letter not in available_letters:
                valid = False
                break
            available_letters.remove(letter)

        if valid:
            score = 0
            for letter in word:
                score += scores[letter]
            valid_words.append((score, word))
    for play in sorted(valid_words):
        print(str(play[0]) + " " + (play[1]))

while True:
    rack = list(input("\nWhat letters do you have in your Scrabble rack?\n--> ").lower())
    if rack == list(".quit"):
        break
    else:
        print("")
        scrabble_cheat()