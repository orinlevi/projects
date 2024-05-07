from copy import deepcopy

#################################################################
# FILE : car.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: class car
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina Eisenbach.
#################################################################


class Car:
	"""
	class of cars (which will be placed in the game board). each car has a
	name, lenght, orientation (position) and location coordinate (-that
	indicates its leftmost and upper part - depending on its orientation.
	"""

	def __init__(self, name, length, location, orientation):
		"""
		A constructor for a Car object
		:param name: A string representing the car's name
		:param length: A positive int representing the car's length.
		:param location: A tuple representing the car's head (row,
		col) location.
		:param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
		"""
		self.name = name
		self.length = length
		self.location = location
		self.orientation = orientation

	def car_coordinates(self):
		"""
		:return: A list of coordinates the car is in
		"""
		row = self.location[0]
		column = self.location[1]
		lst_coordinates = []
		if self.orientation == 1:
			for step in range(self.length):
				lst_coordinates.append((row, column + step))
		if self.orientation == 0:
			for step in range(self.length):
				lst_coordinates.append((row + step, column))
		return lst_coordinates[:]

	def possible_moves(self):
		"""
		:return: A dictionary of strings describing possible movements
		permitted by this car.
		"""
		# For this car type, keys are from 'udrl'
		# The keys for vertical cars are 'u' and 'd'.
		# The keys for horizontal cars are 'l' and 'r'.
		# You may choose appropriate strings.
		# implement your code and erase the "pass"
		# The dictionary returned should look something like this:
		# result = {'f': "cause the car to fly and reach the Moon",
		#          'd': "cause the car to dig and reach the core of Earth",
		#          'a': "another unknown action"}
		# A car returning this dictionary supports the commands 'f','d','a'.
		possible_moves = {'l': "the car can turn left",
		                  'r': "the car can turn right",
		                  'u': "the car can go up",
		                  'd': "the car can go down"}
		if self.orientation == 1:
			return {k: possible_moves[k] for k in ['l', 'r']}
		if self.orientation == 0:
			return {k: possible_moves[k] for k in ['u', 'd']}
		else:
			return deepcopy(possible_moves)

	def movement_requirements(self, movekey):
		"""
		:param movekey: A string representing the key of the required move.
		:return: A list of the locations (tuples) of the cells which must be
		empty in order for this move to be legal.
		"""
		# For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
		# be empty in order to move down (with a key 'd').
		# implement your code and erase the "pass"
		row = self.location[0]
		col = self.location[1]
		length = self.length
		if movekey == 'l':
			return [(row, col - 1)]
		if movekey == 'r':
			return [(row, col + length)]
		if movekey == 'u':
			return [(row - 1, col)]
		if movekey == 'd':
			return [(row + length, col)]

	def move(self, movekey):
		"""
		:param movekey: A string representing the key of the required move.
		:return: True upon success, False otherwise
		"""
		if movekey in self.possible_moves():
			row = self.location[0]
			col = self.location[1]
			if movekey == 'l':
				self.location = (row, col - 1)
			elif movekey == 'r':
				self.location = (row, col + 1)
			elif movekey == 'u':
				self.location = (row - 1, col)
			elif movekey == 'd':
				self.location = (row + 1, col)
		else:
			return False
		return True

	def get_name(self):
		"""
		:return: The name of this car.
		"""
		return self.name
