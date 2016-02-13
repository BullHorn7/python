# This program takes a list and prints it out as a string with 
# commas between each word and 'and' before the last word

spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(listName):
    for i in listName[:-1]:
        print(i, end=", ")
    print("and " + listName[-1])

commaCode(spam)