#A for loop lets you work with item in a list,
#one item at a time.
countries = ['CAN', 'CHL', 'IND', 'AUS']

for country in countries:
	print(f"I'm flying to {country}.")

#Loop through part of a list.
for country in countries[:3]:
	print(f"I've been to {country}.")