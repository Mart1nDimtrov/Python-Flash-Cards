#Default values are helpful because
#they make some arguments optional.

def coffee(size=12):
	"""Serve a cup of coffee."""
	print(f"Here's your {size} oz cup of coffee!")

coffee()
coffee(18)