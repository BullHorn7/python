# Variables to work with
a = 0
b = 0
# List to populate all results
numbers = [1, 2]
# List to populate only the even numbers
evenNumbers = []

# Loop that sums up the last 2 values in the list and repeats until reaching 4mil.
while a + numbers[-2] < 4000000:  
    a = numbers[-2] + numbers[-1]
    numbers.append(a)
# Loop that divides all the numbers in the first list by 2 and only appends numbers
# without any remainder into the second list
for b in numbers:
    if b % 2 == 0:
        evenNumbers.append(b)

print(sum(evenNumbers))
