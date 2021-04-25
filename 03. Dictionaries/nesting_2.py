#Use a list of values in a dictionary.
states_visited = {
	'Eric': ['CA', 'CO', 'CT'],
	'Isaac': ['DE', 'FL', 'GA'],
}

for person, states in states_visited.items():
	print(f'{person} has visited:')
	for state in states:
		print(f' {state}')