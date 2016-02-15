grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Loop through the AMOUNT of values in the [0] sub-list, which is 6
for x in range(len(grid[0])):
	# Loop through the AMOUNT of values in the list, which is 9
	for y in range(len(grid)):
		# Print the content of each sub-list from top-left, going down
		# Once the loop completes 9 iterations, it returns to the 
		# first loop, which goes one step forward and then repeats
		# the 2nd loop on the contents of the next column
		print(grid[y][x], end="")
	# Print at the end of the loop to create a newline
	print()