import math

def is_prime(check_prime):
    for potential_factor in range(2, check_prime):
        divided = check_prime % potential_factor
        if divided == 0:
            return False
    return True

s = int(input("Choose a number and I'll tell you all the prime factors of it, starting from the largest:\n> "))
sqrt = int(math.sqrt(s))
results = []

for potential_factor in range(sqrt, 3, -1):
    divided = s % potential_factor
    if divided == 0 and is_prime(potential_factor) == True:
        results.append(potential_factor)

print(results)