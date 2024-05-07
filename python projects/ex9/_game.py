import sys
import board
import car
from helper import load_json


#################################################################
# FILE : game.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: class car
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina Eisenbach.
#################################################################

LEGAL_CAR_NAMES = ['Y', 'B', 'O', 'G', 'W', 'R']
LEGAL_MOVE_KEY = ['u', 'd', 'l', 'r']
LEGAL_ORIENTATIONS = [0, 1]


class Game:
	"""
	the class of the game itself.
	the game contains a valid board which contains cars.
	in each turn in the game the player can move only one car according to
	the claas Car and class Board rules. the player also can ask for hints-
	possible moves for the cars in the board.
	ones a car arrival the board target coordinate the player win the game.
	the only legal car names in the game are ['Y', 'B', 'O', 'G', 'W', 'R'].
	every car in the game is between a length of 2-4 cells.
	"""

	def __init__(self, board):
		"""
		Initialize a new Game object.
		:param board: An object of type board
		"""
		self.__board = board
		self.__legal_car_names = LEGAL_CAR_NAMES  # the legal names of the
		# cars in the game.
		self.__legal_movekeys = LEGAL_MOVE_KEY  # the legal moves (
		# directions) for the cars in the game.
		self.__end_game = False  # bool param that indicate whether the game
		# should be over for eny reason (victory or the gamer wish).

	def __single_turn(self):
		"""
		Note - this function is here to guide you and it is *not mandatory*
		to implement it.

		The function runs one round of the game :
			1. Get user's input of: what color car to move, and what
				direction to move it.
			2. Check if the input is valid.
			3. Try moving car according to user's input.

		Before and after every stage of a turn, you may print additional
		information for the user, e.g., printing the board. In particular,
		you may support additional features, (e.g., hints) as long as they
		don't interfere with the API.
		"""
		choice = input("choose your move\n")

		if choice == 'hints':
			print(self.__board.possible_moves())

		elif choice == '?':
			print("to make the car move enter the name of the car you"
			      "want to move and the direction you want it to move.\n"
			      "for example: if you want car 'O' to turn right enter O,r\n"
			      "to quite the game enter !\n"
			      "and to get possible moves enter hints\n"
			      "if you will get to the exit cell, you win")

		elif choice == '!':
			print("Bye, Bye")
			self.__end_game = True

		elif len(choice) == 3 and choice[1] == ',' and choice[0] in \
			self.__legal_car_names and choice[2] in self.__legal_movekeys:
			if self.__board.move_car(choice[0], choice[2]):
				if self.__board.cell_content(self.__board.target_location()) is \
					not None:
					print(self.__board)
					print("you won!")
					self.__end_game = True
				else:
					print(self.__board)
					print("interesting, what's your next move?")
			else:
				print("your selection doesn't match the board data")

		else:
			print("Your input is invalid")

	def play(self):
		"""
		The main function of the Game. Manages the game until completion.
		:return: None
		"""
		print("welcome to our game! the rules are simple:\n"
		      "to make the car move enter the name of the car you want to"
		      "move and the direction you want it to move.\n"
		      "for example: if you want car 'O' to turn right enter O,r\n"
		      "to quite the game enter !\n"
		      "and for get possible moves enter hints\n"
		      "if you will get to the exit cell, you win",
		      "for showing those rules again enter ?\n"
		      "have fun and good luck :)\n")
		print(self.__board)
		if self.__board.cell_content(self.__board.target_location()) is \
			not None:
			print("you technically won!")
			self.__end_game = True

		while not self.__end_game:
			self.__single_turn()


if __name__ == "__main__":
	board = board.Board()  # creates an object from type Board - it
	# still has no cars
	arg = sys.argv  # the alias "arg" saves the input from the commend line
	jason_file_name = arg[1]
	cars_to_board: dict = load_json(jason_file_name)  # load the dictionary
	# with the bord's cars data into the alias "cars_to_board"
	for name, val in cars_to_board.items():
		car_length = val[0]
		car_location = (val[1][0], val[1][1])
		car_orientation = val[2]
		# the next few lines check if the data from the "cars_to_board"
		# legal according to the game's rules and if it does the function
		# creates a new object from class Car according to the given data
		# and adds it to the bord (type Board) if its possible according to
		# the board data.
		if 2 <= car_length <= 4 and (name in LEGAL_CAR_NAMES) and \
			(car_orientation in LEGAL_ORIENTATIONS):
			_car = car.Car(name, car_length, car_location, car_orientation)
			board.add_car(_car)
	the_game = Game(board)  # creates an object from type Game - "the_game"
	the_game.play()  # the calling of this function starts the game.
