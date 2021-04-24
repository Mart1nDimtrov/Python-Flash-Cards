#A tuple is an ordered collection of items that can't 
#be modified.
elementary_grades = (2, 3, 4)

#Access an element in the tuple with its index.
print(elementary_grades[0])
print(elementary_grades[:3])
print(elementary_grades[-1])

#Loop through a tuple with the for loop.
for grade in elementary_grades:
	print(f'Welcome to grade {grade}!')

#If you try to modify an element in a tuple
#you'll get an error.

elementary_grades[0] = 1