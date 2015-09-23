s = 0

# Look at all values within '1000' range and assigned them to variable i
for i in range(1000):
    # Divide each number by 3 and 5 and see if either leaves a remainder
    if i % 3 == 0 or i % 5 == 0:
        # If True, add the number to variable s and continue the loop
        s += i
print(s)
