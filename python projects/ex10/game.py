import game_parameters
from apple import *
from bomb import *
from snake import *


#################################################################
# FILE : game.py
# WRITER : orin levi , orin.levi , 206440075 and Pnina_ei Pnina 212125678
# EXERCISE : intro2cs2 ex10 2022
# DESCRIPTION: class game
# STUDENTS I DISCUSSED THE EXERCISE WITH: Orin Levi, Pnina Eisenbach.
#################################################################


class Game:
	"""
	Class game creates a game object. the game contain Bomb,snake and Apples
	(-represented by a dictionary which his keys are the apples coordinates
	and his values are the apple object that fits to those coordinates)
	elements (other objects) that saved in his attributes. His attributes
	also contains score, board's size, how many apple need to be relocated and
	disqualifications variables that indicate whether the snake hit the
	bomb/himself or went out of range and whether the bomb exploded out of range.
	"""
	def __init__(self):
		self.__snake = self.__initial_snake()
		self.__bomb = self.__initial_bomb()
		self.__apples = self.__initial_apples()
		self.__score = 0
		self.__if_snake_out_of_range = False
		self.__board_size = game_parameters.WIDTH * game_parameters.HEIGHT
		self.__apples_to_relocate = 0
		self.__snake_hit_himself = False
		self.__snake_hit_bomb = False
		self.__bomb_exploded_out_of_range = False

	# initials elements
	def __initial_snake(self):  # snake
		"""
		This function initials the snake by creating a snake object and add
		three coordinates so that the head of the snake will be in the center
		of the board
		"""
		snake = Snake()
		w = game_parameters.WIDTH
		h = game_parameters.HEIGHT
		init_coordinates = []
		for num in range(3):
			init_coordinates.append((w//2, h//2 - num))
		for coordinate in init_coordinates[::-1]:  # creating the snake
			snake.add_first(coordinate)
		return snake

	def __initial_bomb(self):  # bomb
		"""
		This method initials the bomb by lottery bomb data and creating a
		bomb object with those data
		The function keeps running until "she finds" snake data that doesn't
		collide (with the coordinates) with the other element the initialised
		firs- the snake.
		"""
		while True:
			a, b, radius, time = game_parameters.get_random_bomb_data()
			if (a, b) not in self.__snake.get_snake_coordinate():
				bomb = Bomb((a, b), radius, time)  # creating
				# the bomb
				break
		return bomb

	def __initial_apples(self):  # apples
		"""
		This method initials the apples dictionary by lottery apples data
		and creating apple objects with those data.
		There should be three apples so until the function succeed to lottery
		three apples which they coordinates doesn't collide with each other,
		with the bomb's coordinates and with the snake's coordinates,
		she keeps running.
		"""
		dictionary_of_apples = {}  # creating dict of apples
		while len(dictionary_of_apples) < 3:
			c, d, score = game_parameters.get_random_apple_data()
			apple = Apple((c, d), score)
			apple_cor = apple.get_coordinate()
			if apple_cor not in dictionary_of_apples.keys() and apple_cor not in \
				self.__snake.get_snake_coordinate() and apple_cor not in \
				self.__bomb.get_coordinate():
				dictionary_of_apples[apple.get_coordinate()] = apple
		return dictionary_of_apples

	# gets elements
	def get_snake(self):
		return self.__snake

	def get_bomb(self):
		return self.__bomb

	def get_apples(self):
		return self.__apples

	def __get_apples_to_relocate(self):
		return self.__apples_to_relocate

	# changes (set) elements
	def new_bomb(self, new_bomb):
		self.__bomb = new_bomb

	def new_apples(self, new_apples):
		self.__apples = new_apples

	def add_score(self, addition):
		self.__score += addition

	def get_score(self):
		return self.__score

	# .......................... the game .......................... #

	# checks_snake_disqualification
	def __if_snake_hit_himself(self):
		"""
		Helper function.
		This method checks if the snake hit himself by calling the game's
		snake object's method "snake_hit_himself()"
		"""
		if self.__snake.snake_hit_himself():
			self.__snake_hit_himself = True

	def do_snake_hit_himself(self):
		"""
		This method checks if the snake hit himself by calling the helper
		function (method) "__if_snake_hit_himself() and returning the Game's
		attribute "__snake_hit_himself".
		"""
		self.__if_snake_hit_himself()
		return self.__snake_hit_himself

	def __if_snake_hit_bomb(self):
		"""
		Helper function.
		This method checks if the snake hit the bomb by checking If there
		is an overlap between the snake's coordinates and the bomb coordinates.
		"""
		for _boom_cor in self.get_bomb().get_coordinate():
			if _boom_cor in self.get_snake().get_snake_coordinate():
				self.__snake_hit_bomb = True

	def do_snake_hit_bomb(self):
		"""
		This method checks if the snake hit the bomb by calling the helper
		function (method) "__if_snake_hit_bomb()" and returning the Game's
		attribute "__snake_hit_bomb_".
		"""
		self.__if_snake_hit_bomb()
		return self.__snake_hit_bomb

	def __snake_out_of_range(self):  # set "snake_out_of_range"
		self.__if_snake_out_of_range = True

	def if_snake_out_of_range(self):  # get "snake_out_of_range"
		return self.__if_snake_out_of_range

	# snake success
	def __snake_eat_apple(self):
		"""
		this function called when the snake ate apple and adds 3 to the game's
		snake object's attribute "__length_to_add" by calling the game's
		snake object's method "set_add_to_snake_length(num)"
		"""
		self.__snake.set_add_to_snake_length(3)

	# bomb
	def __bomb_out_of_range(self):  # set "bomb_out_of_range" to True
		self.__bomb_exploded_out_of_range = True

	def __reset_bomb_out_of_range(self):  # set "bomb_out_of_range" to the
		# variable initial value - False.
		self.__bomb_exploded_out_of_range = False

	def __if_bomb_out_of_range(self):  # get "bomb_out_of_range"
		return self.__bomb_exploded_out_of_range

	def bomb_explosion(self):
		self.get_bomb().explosion()
		if not self.__if_bomb_out_of_range():
			for _boom_cor in self.get_bomb().get_coordinate():
				a, b = _boom_cor
				if (a < 0) or (a > game_parameters.WIDTH - 1) or \
					(b < 0) or (b > game_parameters.HEIGHT - 1):
					self.__bomb_out_of_range()
					break
		self.__check_and_relocate_bomb()

	def __check_and_relocate_bomb(self):
		if self.get_bomb().if_end_of_bomb():
			while True:
				_a, _b, radius, time = game_parameters.get_random_bomb_data()
				if (_a, _b) not in self.get_snake().get_snake_coordinate() and \
					(_a, _b) not in self.get_apples().keys():
					new_bomb = Bomb((_a, _b), radius, time)
					self.new_bomb(new_bomb)
					self.get_bomb().explosion()  # the explosion begins from
					# the firs turn.
					self.__reset_bomb_out_of_range()
					break
		elif self.__if_bomb_out_of_range():
			new_coordinates = []
			for cor in self.get_bomb().get_coordinate():
				a, b = cor
				if (a < 0) or (a > game_parameters.WIDTH - 1) or \
					(b < 0) or (b > game_parameters.HEIGHT - 1):
					continue
				else:
					new_coordinates.append(cor)
			self.get_bomb().set_coordinate(new_coordinates[:])

	# apples
	def check_apples_to_relocate_and_score(self):
		for cor, apple in self.get_apples().items():
			if cor == self.get_snake().get_head_coordinate():
				self.add_score(apple.get_score())
				self.__snake_eat_apple()
				self.__apples_to_relocate += 1
			if cor in self.get_bomb().get_coordinate():
				self.__apples_to_relocate += 1

	def __reset_apples_to_relocate(self):
		self.__apples_to_relocate = 0

	def relocate_apples(self):
		if self.__get_apples_to_relocate() != 0:
			new_dictionary = {}
			for cor, apple in self.get_apples().items():
				if cor in self.get_snake().get_snake_coordinate() or cor in \
					self.get_bomb().get_coordinate():
					while True:
						_c, _d, score = game_parameters.get_random_apple_data()
						new_apple = Apple((_c, _d), score)
						new_apple_cor = new_apple.get_coordinate()
						if new_apple_cor not in self.get_apples().keys() and \
							new_apple_cor not in self.get_snake().get_snake_coordinate() \
							and new_apple_cor not in self.get_bomb().get_coordinate():
							new_dictionary[new_apple.get_coordinate()] = new_apple
							break
				else:
					new_dictionary[cor] = apple
			self.new_apples(new_dictionary)
			self.__reset_apples_to_relocate()

	# checks_disqualification
	def is_board_full(self):
		"""
		this method checks if the board is full by counting all the Game's
		elements coordinates (after verifying that there are no duplicates)
		and the num of apples that need to be relocated and checking if the
		result of the count bigger than the board size (the num of the
		existing coordinates in the board).
		:return True if the board is full.
		"""
		snake_cor = self.get_snake().get_snake_coordinate()
		bomb_cor = self.__bomb.get_coordinate()
		apples_cor = [cor for cor in self.get_apples().keys()]

		full_coordinates = set(snake_cor + bomb_cor + apples_cor)

		if self.__board_size < (len(full_coordinates) +
		                        self.__get_apples_to_relocate()):
			return True
		#  do i need to use with already exploded or cur exploded- I mean
		# bomb.coordinate?

	# user interface
	def key_clicked_change_snake_direction(self, direction):
		"""
		This method changes (set) the Game's snake's direction to the given
		direction only if the current direction is not opposite to it.
		"""
		if (direction == 'Left') and (self.get_snake().get_direction() !=
		                              'Right'):
			self.get_snake().set_direction('Left')
		elif (direction == 'Right') and (self.get_snake().get_direction() !=
		                                 'Left'):
			self.get_snake().set_direction('Right')
		elif (direction == 'Up') and (self.get_snake().get_direction() !=
		                              'Down'):
			self.get_snake().set_direction('Up')
		elif (direction == 'Down') and (self.get_snake().get_direction() !=
		                                'Up'):
			self.get_snake().set_direction('Down')

	def key_clicked_move_snake(self):
		"""
		This method changes (set) the Game's snake's "__head" (head
		coordinate) attribute (by calling to the Game's snake's
		"move_the_snake(cor)" method) according to the currently Game's
		snake's direction but only if new head coordinate is in the board's
		limits. Else, its call the method "__snake_out_of_range()" to change
		the attribute "__if_snake_out_of_range" to True (Which will be used
		later in the file "snake_main.py" to stop the game).
		"""
		x, y = self.__snake.get_head_coordinate()
		if (self.get_snake().get_direction() == 'Left') and (x > 0):
			x -= 1
		elif (self.get_snake().get_direction() == 'Right') and (
			x < game_parameters.WIDTH - 1):
			x += 1
		elif (self.get_snake().get_direction() == 'Up') and (
			y < game_parameters.HEIGHT - 1):
			y += 1
		elif (self.get_snake().get_direction() == 'Down') and (y > 0):
			y -= 1
		else:
			self.__snake_out_of_range()
		self.get_snake().move_the_snake((x, y))
