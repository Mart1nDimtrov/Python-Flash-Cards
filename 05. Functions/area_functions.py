"""A set of functions for calculating areas."""

import math 

def area_rect(w, h):
	"""Calculate the area of a rectangle."""
	area = w * h
	if w >= 0 and h >= 0:
		return area
	else:
		return None

def area_circle(r):
	"""Calculate the area of a circle."""
	area = math.pi * pow(r, 2)
	return area
 