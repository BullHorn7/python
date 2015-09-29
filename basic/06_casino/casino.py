import random

# Defining a Class. It can contain functions that can later be assigned
# to unique cases, without having to re-write code
class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides) 

print("D6 rolls:")
d = Die(6)
print(d.roll())
print(d.roll())
print(d.roll())

print("D20 rolls:")
d2 = Die(20)
print(d.roll())
print(d.roll())
print(d.roll())