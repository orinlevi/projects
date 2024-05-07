from copy import deepcopy
from typing import List


#################################################################
# FILE : snake.py
# WRITER : orin levi , orin.levi , 206440075 and Pnina_ei Pnina 212125678
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: class Snake
# STUDENTS I DISCUSSED THE EXERCISE WITH: Orin Levi, Pnina Eisenbach.
#################################################################

class Node:
	"""
	Class node creates a node object. used as a "class helper" for class
	snake. Every Node has a coordinate attribute that contains its location and
	"prev" and "next" attributes that allows to create linked lists.
	"""

	def __init__(self, coordinate, _next=None, _prev=None):
		self.__coordinate = coordinate
		self.__next = _next
		self.__prev = _prev

	def get_coordinate(self) -> tuple:
		return self.__coordinate

	def set_next(self, _next):
		self.__next = _next

	def set_prev(self, prev):
		self.__prev = prev

	def get_next(self):
		return self.__next

	def get_prev(self):
		return self.__prev


class Snake:
	"""
	Class snake creates a snake object. The snake is implemented as a linked
	list. His head and tail (node objects), moving direction (default- up),
	length (from head to tail including), the length that should be add
	to the snake (one Node every time to the end of the linked list) and
	color (default- black) are saved in a attributes in the __init__.
	"""
	def __init__(self, direction="Up"):
		self.__head = None
		self.__tail = None
		self.__color = "black"
		self.__direction = direction
		self.__length = 0
		self.__length_to_add = 0

	def add_first(self, cor: tuple):
		"""
		The function adds Node that contain the given coordinate (cor) to
		the beginning of the snake, hence the Node become to the snake's new
		head.
		the function also updates the snake's length.
		"""
		vertebra = Node(cor)
		if self.__head is None:
			self.__tail = vertebra
		elif cor != self.get_head_coordinate():
			vertebra.set_prev(self.__head)
			self.__head.set_next(vertebra)
		else:
			return
		self.__head = vertebra
		self.__length += 1

	def remove_last(self):
		"""
		The function removes the snake's tail. If its already None it will
		stay None. If after the removing the tail turned None, the head
		placed to be None too. Else, the Next node become the new tail.
		the function also updates the snake's length.
		"""
		prev_tail = self.__tail
		if self.__tail:
			self.__tail = self.__tail.get_next()
			prev_tail.set_next(None)
			if self.__tail is None:
				self.__head = None
				self.__length = 0
			else:
				self.__tail.set_prev(None)
			self.__length -= 1
		else:
			self.__head = self.__tail = None

	def get_head_coordinate(self):
		"""
		The function returns snake's head's coordinate.
		"""
		return self.__head.get_coordinate()

	def get_tail_coordinate(self):
		"""
		The function returns snake's tail's coordinate.
		"""
		return self.__tail.get_coordinate()

	def set_direction(self, direction: str):
		"""
		The function changes the snake's direction to the given direction.
		"""
		self.__direction = direction

	def get_direction(self):
		"""
		The function returns snake's direction.
		"""
		return self.__direction

	def get_color(self):
		"""
		The function returns snake's color.
		"""
		return self.__color

	def get_snake_coordinate(self) -> List[tuple]:
		"""
		The function returns snake's coordinates (from head to tail).
		"""
		coordinate = []
		vertebra = self.__head
		while vertebra:
			coordinate.append(vertebra.get_coordinate())
			vertebra = vertebra.get_prev()
		return deepcopy(coordinate)

	def get_snake_length(self):
		"""
		The function return snake's length.
		"""
		return self.__length

	def set_add_to_snake_length(self, addition):
		"""
		The function adds to the attribute "length_to_add" the given
		additional.
		"""
		self.__length_to_add += addition

	def __get_length_to_add(self):
		"""
		The function return snake's length to add.
		"""
		return self.__length_to_add

	def __reduce_length_to_add(self):
		"""
		The function decreases snake's length to add by 1.
		"""
		self.__length_to_add -= 1

	def move_the_snake(self, cell):
		"""
		The function moves the snake toward the snake's direction by adding
		a Node with the given coordinate (cell) to the beginning of the snake
		and removing snake's tail unless the length to add is not 0.
		"""
		self.add_first(cell)
		if self.__get_length_to_add() == 0:
			self.remove_last()
		else:
			self.__reduce_length_to_add()

	def snake_hit_himself(self):
		"""
		The function checks if the snake hit himself by checking if there is a
		coordinate that appears more than ones in snake's self coordinates.
		"""
		snake_coordinate = self.get_snake_coordinate()
		if snake_coordinate.count(self.get_head_coordinate()) > 1:
			return True

