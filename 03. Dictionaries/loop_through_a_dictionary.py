#Default behavior for looping through 
#a dictionary is using the keys.
capitals = {
	'AK': 'Juneau',
	'AL': 'Montgomery',
	'AZ': 'Phoenix',
}

for state in capitals:
	print(f'State: {state}')

#Access the values in a dictionary.
for capital in capitals.values():
	print(f'Capital: {capital}')

#Access both key and value.
for state, capital in capitals.items():
	print(f'{capital}, {state}')
