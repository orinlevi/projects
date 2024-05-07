#################################################################
# FILE : apple.py
# WRITER : orin levi , orin.levi , 206440075 and Pnina_ei Pnina 212125678
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: class Apple
# STUDENTS I DISCUSSED THE EXERCISE WITH: Orin Levi, Pnina Eisenbach.
#################################################################

class Apple:
	"""
	Class apple creates an apple object. the class has three "geters" methods
	that's are giving back the apple's attributes- apple's coordinate,
	the score that given when eating the apple and apple's color
	"""

	def __init__(self, coordinate, score):
		self.__coordinate = coordinate
		self.__score = score
		self.__color = "green"

	def get_coordinate(self):
		"""
		:return coordinates
		the methods return the coordinates of the apple
		"""
		return self.__coordinate

	def get_color(self):
		"""
		:return color of the apple
		the methods return the color of the apple
		"""
		return self.__color

	def get_score(self):
		"""
		:return score
		the methods return the score of the apple
		"""
		return self.__score
