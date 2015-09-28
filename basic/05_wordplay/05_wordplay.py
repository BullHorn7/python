# This is going to be a simple program that will only perform
# a number of actions. I plan to re-iterate this in the future 
# into a full-fledged scrabble cheater

# Creates a list from all the values in sowpods.txt
scrabble_dict = []
dictionary = open("sowpods.txt", "r")
for line in dictionary:
    stripped_line = line.strip()
    lower_case_line = str.lower(stripped_line)
    scrabble_dict.append(lower_case_line)
dictionary.close()

# Prints all the words that have "uu" in them
for word in scrabble_dict:
    if "uu" in word:
        print(word)

# Defines a function to 
letters = "abcdefghijklmnopqrstuvwxyz"
def has_a_double(letter):
    for word in scrabble_dict:
        if letter + letter in word:
            return True
    return False
# Prints which letters never appear twice in a row in a word
for letter in letters:
    if not has_a_double(letter):
        print(letter + " never appears doubled")