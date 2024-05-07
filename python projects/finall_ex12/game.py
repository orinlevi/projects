from copy import deepcopy

import boggle_board_randomizer as bbr
import ex12_utils as utils_12


class Game:
    """
     this class is the game 'boggle'
    """

    def __init__(self):
        self.__board = bbr.randomize_board()
        self.__board_words = utils_12.load_words()  # the words list from the
        # boggle_dict
        self.__score = 0
        self.__found_words = []
        self.__cur_word = "word: "
        self.__cur_path = []

    def get_board(self):
        """
        the method return a copy of the board
        :return: the board
        """
        return deepcopy(self.__board)

    def get_score(self):
        """"
        :return: score
        """
        return self.__score

    def __add_score(self, path):
        """
        the method gets a path - list of tuple and calculates the score the
        player got by raise to the power the length of the path and update it
        :param path:
        """
        self.__score += len(path) ** 2

    def __get_found_words(self):
        """"
        :return: a copy of the list of the found words
        """
        return deepcopy(self.__found_words)

    def __add_to_found_words(self, new_word):
        """"
        the method add to the list of the found word a new word the player
        found
        :param: new word
        """
        self.__found_words.append(new_word)

    def get_cur_word_to_display(self):
        """
         the method return the word the player found in lower letters
        """
        return self.__cur_word.lower()

    def __set_cur_word(self, letter):
        """
        the method gets a letter and adding it to the string word the player is
        forming
        :param letter:
        """
        self.__cur_word += letter

    def add_to_cur_word(self, coordinate):
        """
        the method receive a converted letter and adding it to the word
        :param coordinate: tuple that represent a letter on the board
        """
        letter = utils_12.create_word([coordinate], self.get_board())
        self.__set_cur_word(letter)

    def __get_path(self):
        """
        the method return a copy of the path - list if tuples that represents
        a path on the board
        :return: a path
        """
        return deepcopy(self.__cur_path)

    def add_cor_to_path(self, coordinate):
        """
        the method add a coordinate to the list of tuples that are the path
        on the board
        """
        self.__cur_path.append(coordinate)

    def __get_board_words(self):
        """
        the method return a copy of the list of all the words that can be
        show on the board
        :return: list of words
        """
        return deepcopy(self.__board_words)

    def __reset_cur_word_and_path(self):
        """
        the method reset the screen where the player is form the word
        and it also reset the path to a giving word
        """
        self.__cur_word = "word: "
        self.__cur_path = []

    def reset(self):
        """
        the method reset the game including the board the timer, the score and
        the list of the found word the player has accumulate
        """
        self.__found_words = []
        self.__score = 0
        self.__reset_cur_word_and_path()
        self.__board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                        ["", "", "", ""]]

    def check_paths(self):
        """"
        the method check if a path on the board os valid and if so return the
        word the player formed and reset the screen where it displayed and
        reset the list of the coordinates of the word
        """
        word = utils_12.is_valid_path(self.get_board(), self.__get_path(),
                                      self.__get_board_words())
        if word:
            if len(word) > 1 and word not in self.__get_found_words():
                self.__add_to_found_words(word)
                self.__add_score(self.__get_path())
                self.__reset_cur_word_and_path()
                return word.lower()
        self.__reset_cur_word_and_path()

    def instructions(self):
        """
        the method returns the instructions of the game
        """
        inst = "welcome to boggle game\n the instructions are pretty simple: " \
               "\n""Find the words that are hidden in the board.\n Words that" \
               " have ""the exact spelling but \n different meanings will " \
               "be counted ""only once.\n You cannot repeat any word \n and" \
               " you are allowed ""to \n " "move left, right, up, down and in" \
               " diagonal \n ho and you ""have 3 minutes \n" "good luck! :)"
        return inst
