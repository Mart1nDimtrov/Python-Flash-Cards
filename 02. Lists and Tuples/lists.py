#A list is a collection of items in a specific order.
#Square brackets indicate a list.

#Access items in the list through the index.
vowels = ['e', 'i', 'o']
print(vowels[0])
print(vowels[-1])

#Append an item to the end of the list.
vowels.append('a')
print(vowels)

#Insert anywhere in the list.
vowels.insert(0, 'u')
print(vowels)

#Modify an element using its index.
vowels[-1] = 'u'
vowels[0] = 'a'
print(vowels)