from copy import deepcopy

#################################################################
# FILE : bomb.py
# WRITER : orin levi , orin.levi , 206440075 and Pnina_ei Pnina 212125678
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: class Bomb
# STUDENTS I DISCUSSED THE EXERCISE WITH: Orin Levi, Pnina Eisenbach.
#################################################################


class Bomb:
	"""
	Class game creates a game object. The bomb's color, radius (remain
	radius to the explosion), time until the explosion should start,
	coordinates, and "already exploded coordinates (the coordinates of all the
	levels of the bomb - prev and current) are saved in a attributes in the
	__init__. In addition, there are two bool attribute that indicates
	whether the explosion already begin and whether it already over (
	"__explosion_began" and "__end_of_bomb").
	"""

	def __init__(self, coordinate: tuple, radius, time):
		self.__color = "red"
		self.__coordinate = [coordinate]
		self.__radius = radius
		self.__time = time
		self.__explosion_began = False
		self.__already_exploded = []
		self.__end_of_bomb = False

	def set_coordinate(self, new_coordinates):
		"""
		This method set the bomb's coordinates to the given coordinates.
		"""
		self.__coordinate = deepcopy(new_coordinates)  # deep_copy to
	# prevent access to the memory of the bomb's list of coordinates.

	def get_coordinate(self):
		return deepcopy(self.__coordinate)

	def __add_already_exploded(self, lst_of_coordinates):
		self.__already_exploded += deepcopy(lst_of_coordinates)

	def get_already_exploded(self):
		"""
		This function return a deepcopy of the bomb's list of already
		exploded coordinates.
		"""
		return deepcopy(self.__already_exploded)

	def __set_explosion_coordinates(self):
		new_coordinate = []
		for cor in self.get_coordinate():
			x, y = cor
			new_coordinate += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
		_new_coordinate = set([cor for cor in new_coordinate if cor not in
		                       self.get_already_exploded()])
		self.set_coordinate(list(_new_coordinate))
		self.__add_already_exploded(list(_new_coordinate))

	def __reduce_remain_radius(self):
		self.__radius -= 1

	def __get_radius(self):
		return self.__radius

	def __set_color(self, new_color):
		self.__color = new_color

	def get_color(self):
		return self.__color

	def __reduce_remain_time(self):
		self.__time -= 1

	def __get_time(self):
		return self.__time

	def __start_explosion(self):
		self.__explosion_began = True

	def __get_explosion_mode(self) -> bool:
		return self.__explosion_began

	def end_of_bomb(self):
		self.__end_of_bomb = True

	def if_end_of_bomb(self):
		return self.__end_of_bomb

	def explosion(self):
		"""
		This method starts and promotes the explosion of the bomb
		"""
		if self.__get_time() > 0:
			self.__reduce_remain_time()  # as long as there is more time until the
			# explosion should start it reduces the remain time in one.
			return
		elif self.__get_time() == 0:
			if self.__get_explosion_mode():
				if self.__get_radius() == 0:
					self.end_of_bomb()
					return
				else:
					self.__set_explosion_coordinates()
					self.__reduce_remain_radius()
			else:
				self.__start_explosion()
				self.__set_color("orange")  # when the explosion starts the
				# color of the bomb turns orange
				self.__add_already_exploded(self.get_coordinate())

