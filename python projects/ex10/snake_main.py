import game_display
from game_display import GameDisplay
from game import *


#################################################################
# FILE : snake_main.py
# WRITER : orin levi , orin.levi , 206440075 and Pnina_ei Pnina 212125678
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: the main loop for the game
# STUDENTS I DISCUSSED THE EXERCISE WITH: Orin Levi, Pnina Eisenbach.
#################################################################


def display_elements(gd: GameDisplay, game: Game, do_snake_hit_bomb: bool):
	"""
	This function displays the elements of the game.
	If the snake hit the bomb it shows only the snake's coordinates that
	doesn't heat the bomb.
	"""

	gd.show_score(game.get_score())  # score

	snake_cor = set(game.get_snake().get_snake_coordinate())  # snake
	# the set is to avoid duplicates in the GUI's display in case that the
	# snake hit himself (and has the same coordinate twice - his head and
	# tail are the same)
	if do_snake_hit_bomb:
		bomb_cor = game.get_bomb().get_coordinate()
		new_snake_cor = [cor for cor in snake_cor if cor not in bomb_cor]
		snake_cor = new_snake_cor
	for cell in snake_cor:
		a, b = cell
		gd.draw_cell(a, b, game.get_snake().get_color())

	for boom_cor in game.get_bomb().get_coordinate():  # bomb
		boom_x, boom_y = boom_cor
		gd.draw_cell(boom_x, boom_y, game.get_bomb().get_color())

	for cor, apple in game.get_apples().items():  # apples
		_x, _y = cor
		gd.draw_cell(_x, _y, apple.get_color())


def main_loop(gd: GameDisplay) -> None:
	"""
	this function runs the game and connect it to the GUI.
	For start, its creates a Game object and display the initial board.
	From then on, its checks if the user clicked on one of the movement keys in
	the keyboard, changes the snake's direction in accordance and moves the snake
	toward his currently direction. After that, if the snake didn't hit the
	bomb coordinates or himself, It promotes the explosion of the bomb.
	Than it checks if there apples that need to be relocated (eaten by
	the snake or was hit by the bomb) and if there is a place on the
	board to place them. If there isn't a place for apple that need to be
	relocate its display the Game's element and end the game. Else,
	if there is apples to relocate, its relocates them and if there isn't
	its continue to the next step.
	To finish, the function display the Game's elements and checks if there
	is disqualification- if there is it's end the game and if not it's
	continue to the next turn.
	"""
	"""this function is the main function that run the game. the rounds of
	the game are shown here. the initiate of the objects start before the
	rounds of the game. the apple located in random places and also the
	bomb. the snake is located on the center of the board"""

	game = Game()
	game.bomb_explosion()
	display_elements(gd, game, False)
	gd.end_round()

	while True:
		key_clicked = gd.get_key_clicked()  # updates_snake
		game.key_clicked_change_snake_direction(key_clicked)
		game.key_clicked_move_snake()

		if not (game.do_snake_hit_himself() or game.do_snake_hit_bomb()):
			game.bomb_explosion()  # updates_bomb

		game.check_apples_to_relocate_and_score()  # updates score from
		# apples and counts how many apples should be relocated.
		if game.is_board_full():  # checks_empty_space_in_board
			display_elements(gd, game, game.do_snake_hit_bomb())
			gd.end_round()
			break  # if there isn't empty space in the board but
			# there is apples that need to be relocated the game is over.
		game.relocate_apples()  # updates_apples

		display_elements(gd, game, game.do_snake_hit_bomb())

		# checks_disqualification
		if game.do_snake_hit_himself() or game.do_snake_hit_bomb() or \
			game.if_snake_out_of_range():
			gd.end_round()
			break  # if there is disqualification the game is over

		gd.end_round()


if __name__ == '__main__':
	gd = GameDisplay()
	main_loop(gd)
