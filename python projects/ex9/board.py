from copy import deepcopy


#################################################################
# FILE : car.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: class car
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina Eisenbach, Noya Hoshkover.
#################################################################


class Board:
	"""
	class of boards.
	the boards size is 7x7 plus extra cell:
	each board divided into cells - 7 cells in a row and 7 in a column
	plus an additional cell at the end of row 4 that used as a target
	coordinate (-latter in game class, arrival of a car to this coordinate
	will lead to a victory). these cells are the board area and any
	location other than them is outside the board boundaries.
	cars from class Car can be placed on the board as long all the cars are
	in the board limits and there are no cells that house used for more than
	one car (-This means that cars cannot be placed one on top of the other).
	each car can move (according to the limits of class Car) in the board
	as long as it does not go beyond the board limits and does not crush other
	cars -that means other cars that are placed on the board are used as
	stopping conditions for each other.
	"""

	def __init__(self):
		# implement your code and erase the "pass"
		# Note that this function is required in your Board implementation.
		# However, is not part of the API for general board types.
		self.__length = 7  # the board height
		self.__width = 7  # the board width
		self.__board = self.__create_board()  # use the function
		# "create_board" to create an empty board according to the board
		# dimensions.
		self.__cars = {}  # dictionary contains the board's cars as a keys
		# and the objects Car (from class Car) which represents those cars
		# (according to their names) as values.
		self.__board_cells = self.cell_list()  # the board's coordinates

	def __create_board(self):
		"""
		this function create an empty board according to the board
		dimensions (dimensions data in the __init__ function).
		:return: a 2D list with the string '_  ' represent an empty cells.
		the list len is the board height and each internal list represent a
		row of the board and its len is the width of the board's row with the
		same index.
		"""
		board = [[] for _ in range(self.__length)]
		for row in range(self.__length):
			for col in range(self.__width + 1):
				if row == (self.__length - 1) / 2 and col == self.__width:
					board[row].append('_  ')
				elif col != self.__width:
					board[row].append('_  ')
		return board

	def __str__(self):
		"""
		This function is called when a board object is to be printed.
		:return: A string of the current status of the board
		"""
		# The game may assume this function returns a reasonable representation
		# of the board for printing, but may not assume details about it.
		str_board = ""
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				str_board += self.__board[row][col]
			str_board += "\n"
		return str_board

	def cell_list(self):
		""" This function returns the coordinates of cells in this board
		:return: list of coordinates
		"""
		# In this board, returns a list containing the cells in the square
		# from (0,0) to (6,6) and the target cell (3,7)
		# coordinates = []
		coordinates = []
		for row in range(len(self.__board)):
			for col in range(len(self.__board[row])):
				coordinates.append((row, col))
		return coordinates[:]

	def possible_moves(self):
		""" This function returns the legal moves of all cars in this board
		:return: list of tuples of the form (name,movekey,description)
		representing legal moves
		"""
		# From the provided example car_config.json file, the return value could be
		# [('O','d',"some description"),('R','r',"some description"),('O',
		# 'u',"some description")]
		possible_moves = []
		for car_name, car in self.__cars.items():
			for movekey, description in car.possible_moves().items():
				empty_cells_req = car.movement_requirements(movekey)
				all_empty = True  # until it proved otherwise
				for cell in empty_cells_req:
					if self.cell_content(cell) is None and cell in \
						self.__board_cells:
						continue
					else:
						all_empty = False
				if all_empty:
					possible_moves.append((car_name, movekey, description))
		return possible_moves[:]

	def target_location(self):
		"""
		This function returns the coordinates of the location which is to be
		filled for victory.
		:return: (row,col) of goal location
		"""
		return int((self.__length - 1) / 2), self.__width

	def cell_content(self, coordinate):
		"""
		Checks if the given coordinates are empty.
		:param coordinate: tuple of (row,col) of the coordinate to check
		:return: The name if the car in coordinate, None if empty
		"""
		if coordinate in self.__board_cells:
			row = coordinate[0]
			col = coordinate[1]
			if self.__board[row][col] != '_  ':
				return self.__board[row][col][:-2]  # if the square isn't
			# empty it means that there is a car name to return and the name
			# is the coordinate string minos the '  ' added to the end.
			else:
				return None

	def add_car(self, car):
		"""
		Adds a car to the game.
		:param car: car object of car to add
		:return: True upon success. False if failed
		"""
		# Remember to consider all the reasons adding a car can fail.
		# You may assume the car is a legal car object following the API.
		# can also be implement with backtracking.
		board = deepcopy(self.__board)
		coordinates = car.car_coordinates()
		for cor in coordinates:
			if (car.get_name() not in self.__cars.keys()) and (
				self.cell_content(cor) is None) and cor in self.__board_cells:
				board[cor[0]][cor[1]] = car.get_name() + '  '
			else:
				return False
		self.__board = board
		self.__cars[car.get_name()] = car
		return True

	def __remove_car_cor(self, coordinates):
		"""
		the function clears the car's old coordinates - replace the
		coordinate's content with the string '_  ' represent an empty cell.
		:param coordinates: the car's old coordinates
		:return: None
		"""
		for cor in coordinates:
			row = cor[0]
			col = cor[1]
			self.__board[row][col] = '_  '

	def __move_car_cor(self, coordinates, name):
		"""
		the function place the car according to the car's new coordinates in
		the board - replaces every string '_  ' represent an empty cell with
		the string of the car's name.
		:param coordinates: the car's new coordinates
		:param name: the name of the car
		:return: None
		"""
		for cor in coordinates:
			row = cor[0]
			col = cor[1]
			self.__board[row][col] = name + '  '

	def move_car(self, name, movekey):
		"""
		moves car one step in given direction.
		:param name: name of the car to move.
		:param movekey: string of the direction to move the car to.
		:return: True upon success, False otherwise.
		"""
		if name in self.__cars.keys():
			car = self.__cars[name]
			if (movekey in car.possible_moves().keys()) and \
			(name, movekey, car.possible_moves()[movekey]) in self.possible_moves():
				self.__remove_car_cor(car.car_coordinates())
				car.move(movekey)
				self.__move_car_cor(car.car_coordinates(), name)
				return True
		return False
