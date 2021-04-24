#Remove a specific item from the list.
airports = ['ANC', 'JNU', 'SEA', 'SIT']
airports.remove('SEA')
print(airports)

#Delete an item from a specific position.
del airports[2]
print(airports)

#Remove the last item and return it.
airport = airports.pop()
print(airport)

#Remove an item from a specific position and return it.
airport = airports.pop()
print(airport)