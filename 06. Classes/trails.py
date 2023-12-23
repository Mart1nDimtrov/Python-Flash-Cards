#Classes store information and actions at the same place. 
class Trail():
	"""A class to represent trails."""
	def __init__(self, dest, len=0):
		self.dest = dest
		self.len = len

	def describe_trail(self):
		"""Print a description of a trail."""
		desc = f"This trail goest to {self.dest}."
		if self.len:
			desc += f"\nThe trail is {self.len}km."
		print(desc)
	def run_trail(self):
		"""Simulate running the trail."""
		print(f"Running to {self.dest}.")

class BikeTrail(Trail):
	"""Represents a bike trail."""

	def __init__(self, dest, len=0):
		super().__init__(dest, len)
		self.paved = True
		self.bikes_only = True

	def ride_trail(self):
		"""Simulate riding the trail."""
		print(f"Riding to {self.dest}.")

	def run_trail(self):
		"""Simulate running the trail."""
		if self.bikes_only:
			print("You can't run this trail!")
		else:
			#We can use the super for intheriting the behaviour
			#of the parent class.
			super.run_trail()