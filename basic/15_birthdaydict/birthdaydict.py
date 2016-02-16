birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	print("Enter a name (blank to quit)\n>>>")
	name = input()
	if name == "":
		break

	if name in birthdays:
		print(name + "'s birthday is on " + birthdays[name])

	else:
		print("I do not know that name")
		print("When is their birthday?\n>>>")
		bday = input()
		birthdays[name] = bday