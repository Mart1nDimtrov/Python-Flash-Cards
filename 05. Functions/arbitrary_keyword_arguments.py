#Placing a double asterisk (**) before a parameter 
#allows a function to accept an arbitrary number 
#of keyword arguments. 
def desc_user(user, **desc):
	"""Describe a user."""
	print(f"Description of {user}")
	for key, value in desc.items():
		print(f"{key}: {value}")

desc_user('anton', active=True,
 email='anton@example.com',
 num_posts=578)