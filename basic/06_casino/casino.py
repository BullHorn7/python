import random

# Defining a Class. It can contain functions that can later be assigned
# to unique cases, without having to re-write code
class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.rantint(1, self.sides) 