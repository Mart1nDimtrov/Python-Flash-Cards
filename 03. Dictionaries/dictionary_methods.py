#Use the get() method to return the value
#associated with a key.
capitals = {
	'AK': 'Juneau',
	'AL': 'Montgomery',
	'AZ': 'Phoenix',
}

print(capitals.get('AK'))
print(capitals.get('WY'))
print(capitals.get('WY', 'unknown'))

#Return different aspects of the dictionary.
print(capitals.keys())
print(capitals.values())
print(capitals.items())