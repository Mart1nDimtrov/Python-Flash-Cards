#When a function needs more than one value we use 
#positional arguments.
def post_msg(msg, user):
	"""Post a message from a user."""
	print(f'{user}: {msg}')

post_msg("I love the internet!", "Willie")