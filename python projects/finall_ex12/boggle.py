from boggle_game import BoggleGUI
from game import Game


class MainGame:
	"""
	this class is the main class where the game itself and the GUI get combined
	the class lets the player to watch the game in graphical way
	"""
	def __init__(self):
		self.game = Game()
		self.gui = BoggleGUI()
		self.gui.set_button_cmd("instructions", lambda:

		self.gui.game_instructions(self.game.instructions()))
		self.gui.set_button_cmd("start", self.start_button_cmd())

	def start_button_cmd(self):
		"""
		the method initiates the 'start' button and gibe if an actions to
		preformed. the method initiate the start button to restart if the
		player press the button before the time ended and in case the time
		over it restart the game by initiate the whole board and the times
		"""

		def _start_button_cmd():
			if self.gui.start_before_finish():
				return
			else:
				self.gui.reset_game()
				self.gui.time_loop_on()
				self.board_buttons()
				self.enter_button()
				self.game = Game()
				board = self.game.get_board()
				self.gui.display_board(board)
				self.gui.change_start_to_restart()
				self.gui.time()
				return
		return _start_button_cmd

	def board_buttons(self):
		"""
		the method set an actions to the board buttons where the letter are on
		"""
		for button_name in self.gui.get_board_buttons().keys():
			self.gui.set_button_cmd(button_name, self.board_button_cmd(button_name))

	def board_button_cmd(self, button_name):
		"""
		the method get a specific button and gets the info of that buttons -
		it add the coordinates to the path list and add the letter that in
		those coordinates to the word the player is forming and display it
		:param button_name:
		"""
		def _board_button_cmd():
			self.game.add_cor_to_path(button_name)
			self.game.add_to_cur_word(button_name)
			self.gui.display_cur_word(self.game.get_cur_word_to_display())
		return _board_button_cmd

	def enter_button(self):
		"""
		the method set an action to the 'enter' button
		"""
		self.gui.set_button_cmd("Enter", self.enter_button_cmd())

	def enter_button_cmd(self):
		"""
		the method sets the action to the 'enter' button. when the player
		finished to form a word that he searched the word is shown on the screen
		"""

		def _enter_button_cmd():
			word = self.game.check_paths()
			if word:
				self.gui.display_found_word(word)
				self.gui.set_score(self.game.get_score())
			self.gui.display_cur_word(self.game.get_cur_word_to_display())
		return _enter_button_cmd


	def start(self):
		"""
		the method start the game
		"""
		self.gui.start_game()

if __name__ == '__main__':
	y = MainGame()
	y.start()
