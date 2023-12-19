#Аn asterisk (*) before a parameter name allows
#a function to receive any number of positional arguments.
def post_messages(user, *msgs):
	"""Post all of a user's messages."""
	print(f"{user} said:")
	for msg in msgs:
		print(f" {msg}")

post_messages('Ahna', "I love mountains.",
 "I love rivers.",
 "I love the ocean.")