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

# Defines a function to scan each word in the list of words
# and determine whether there is a letter that never repeats 
# more than once in a row 
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

# Defined a function to scan each word in the list of words
# and determine whether there is a word that includes all the vowels
vowels = "aeiou"
def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True
# Prints all words that returned True in the function we defined
for word in scrabble_dict:
    if has_all_vowels(word):
        print(word)