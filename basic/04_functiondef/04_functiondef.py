# Let's define a function that takes a word as an argument
# and checks if it starts with a vowel
def is_start_with_vowel(word):
    return word[0] in "AEOUI"

names = ["Archibald", "Beelzebob", "Chupakabra", "Drizzt", "Elreon"]

# Let's define another function that takes a list of words 
# and uses the function that we defined above to loop through the list
def filter_vowel_words(word_list): 
    vowel_words = []
    for word in word_list:
        if is_start_with_vowel(word):
            vowel_words.append(word)
    return vowel_words

print(filter_vowel_words(names))