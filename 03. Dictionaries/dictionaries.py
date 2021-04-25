#A dictionary is a set of items; each item consists of 
#a key and a value.
capitals = {
	'AK': 'Juneau',
	'AL': 'Montgomery',
	'AZ': 'Phoenix',
}

#Access a value using its key.
print(capitals['AK'])

#Add a value again using its key.
capitals['AR'] = 'Little Rock'
print(capitals['AR'])

#Remove items using the del keyword.
del capitals['AR']
print(capitals)