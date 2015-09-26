import sys
import random

if len(sys.argv) < 2:
    print("Please supply a flashcard file name.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

question_dict = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    question_dict[question] = answer

f.close()

print("Welcome to the flashcard quizzer.")
print("Type 'quit' to quit the game.\n")

questions = list(question_dict.keys())

score = 0
count = 0
while True:
    question = random.choice(questions)
    answer = question_dict[question]
    print("What's the capital of: " + question)
    user_input = input("Your answer: ")
    if user_input == "quit":
        print("Thanks for playing!")
        break
    elif user_input == answer:
        count += 1
        print("That's right!")
        score += 1
    else:
        count += 1
        print("Nope! The right answer is:\n> " + answer)

result = count / (score+1)
if result <= 1 and count >= 5:
    print("Well done! You're a legend!")
elif result >= 3:
    print("Wow, dude. You suck.")
else:
    print("Nice try.")
print("You got " + str(score) + " right answers in " + str(count) + " tries.")