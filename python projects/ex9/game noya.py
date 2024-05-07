#####################################################
# FILE : game.py
# WRITER : noya_hoshkover , noya275 , 209110881
# EXERCISE : intro2cs2 ex9 2022
# DESCRIPTION : recreating the 'rush hour' game; class Game
#####################################################


from helper import load_json
import board as board_class
import car as car_class
import sys


class Game:
    """The game contains an empty board at first.
    cars are added according to json file content and if they're legal
    (explained in class Board's description)
    the player can move one car each turn according to the rules.
    the player can also ask for his possible moves for the cars.
    when a car arrives to the board exit coord the player wins the game."""

    def __init__(self, board):
        """Initialize a new Game object.
        :param board: An object of type board"""
        self.__legal_car_names = {'Y', 'B', 'O', 'G', 'W', 'R'}
        self.__legal_movekeys = {'r', 'l', 'u', 'd'}
        self.__board = board

    def __single_turn(self):
        """This function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API."""
        # displays the initial game board
        print(self.__board)
        # if a car was placed at the target cell the player wins technically
        if self.__board.cell_content(self.__board.target_location()
                                     ) is not None:
            print('Technical victory! a car was placed at the exit cell.')
            return False
        # instructions for the player
        user_input = input('To move a car, enter the name of the car you '
                           'would like to move \n'
                           'and the direction in which you would like it to '
                           'move with a comma between them \n'
                           'To quit the game, enter ! \n'
                           'To receive possible moves, enter ? \n')
        # displays help / exits the game - according to user's input
        if user_input == '!':
            return False
        elif user_input == '?':
            print(self.__board.possible_moves())
        # if user's input is valid, continues to check board situation
        elif user_input[0] in self.__legal_car_names and user_input[2] in \
                self.__legal_movekeys:
            # if moving the car is possible - moves car
            if self.__board.move_car(user_input[0], user_input[2]):
                # if a car arrives to the exit cell - the player wins
                if self.__board.cell_content(self.__board.target_location()
                                             ) is not None:
                    print(self.__board)
                    print('Congratulations! you won.')
                    return False
        # if user's input is invalid - raises an error, waits for another input
        else:
            print('Your input is invalid, try again!')

    def play(self):
        """The main driver of the Game. Manages the game until completion.
        stops the game if there is a technical win, or if the player asks
        to quit, or if the player wins.
        :return: None"""
        while True:
            if self.__single_turn() is False:
                break


if __name__ == "__main__":
    legal_car_names = {'Y', 'B', 'O', 'G', 'W', 'R'}
    legal_orientation = {0, 1}
    legal_car_length = {2, 3, 4}
    game_board = board_class.Board()
    arguments = sys.argv
    json_file = arguments[1]
    cars = load_json(json_file)
    # implements data from json file
    for name, data in cars.items():
        car_length = data[0]
        car_orientation = data[2]
        car_location = (data[1][0], data[1][1])
        # checks validity of each car in json file, adds to board only if valid
        if car_length in legal_car_length and name in legal_car_names and \
                car_orientation in legal_orientation:
            car_to_add = car_class.Car(name, car_length, car_location,
                                       car_orientation)
            game_board.add_car(car_to_add)
    # initiates the game
    game = Game(game_board)
    game.play()
