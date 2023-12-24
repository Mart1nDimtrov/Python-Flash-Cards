import unittest
import sys
import os
#Import the path where the modules you are going
#to test are located.
sys.path.insert(0, os.path.abspath("C:\\Users\\LENOVO\\Desktop\\Python-Flash-Cards\\05. Functions"))
import area_functions as af

class AFTestCase(unittest.TestCase):
	"""Test for area_functions.py"""

	def setUp(self):
		"""Create widths and lengths for all tests."""
		self.width = 3
		self.length = 4

	def test_rect_area(self):
		"""Test a simple rectangle."""
		area = af.area_rect(self.width, self.length)
		self.assertEqual(area, 12)

	def test_negative_inputs(self):
		"""Test negative inputs"""
		area = af.area_rect(-3, 4)
		self.assertEqual(area, None)

if __name__ == '__main__':
	unittest.main()