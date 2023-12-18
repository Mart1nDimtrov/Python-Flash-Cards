while True:
	name = input("What's your name? ")
	if name == 'quit':
		break
	print(f"Hello, {name}!")

#The continue keyword breaks the loop and returns to the 
#beginning of the loop:
while True:
	age = input("What's your age? ")
	age = int(age)
	if age < 0:
		print("That makes no sense!")
		continue
	print(f'{age} is a great age!')
	break