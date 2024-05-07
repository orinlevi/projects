#####################################
# FILE : lab4.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 lab4 2021
# DESCRIPTION: programing a "nim" game.
# an assignment in pairs - worked with Pnina Eisenbach.
#####################################


MATCH = '*'
NUM_OF_ROWS = 5
NUM_OF_COL = 4
PLAYER_ONE = 1
PLAYER_TWO = 2


def init_board():
    """
    creating board
    :return: list which represent the board
    """
    board = [NUM_OF_COL] * NUM_OF_ROWS
    return board


def get_next_player(current_player):
    """
    switch between the players
    :param current_player:
    :return: int which represent the player num
    """
    if current_player == PLAYER_TWO:
        return PLAYER_ONE
    else:
        return PLAYER_TWO


def print_board(board):
    """
    the func prints the board
    :param board:
    :return: none
    """
    for i in range(NUM_OF_ROWS):
        print(str(i), ':', end='\t')
        print(MATCH * board[i])


def is_board_empty(board):
    """
    checking whether the board is empty
    :param board:
    :return: bool- true if the board is empty ad false otherwise
    """
    for i in range(NUM_OF_ROWS):
        if board[i] > 0:
            return False
    return True


# constant messages
MESSAGE_ROW_NUMBER_REQUEST = "Please enter row number:"
MESSAGE_AMOUNT_REQUEST = "Please enter the amount to take from row number {} :"
ERROR_NO_SUCH_ROW_OR_EMPTY_ONE = "Illegal row number or an empty row"
ERROR_ILLEGAL_AMOUNT = "Illegal amount"


def get_input(board):
    """
    gets the num of the row and the num of the matches that the player wants
    to remove from this row
    :param board: the board of the game
    :return: valid move of the game that contain num of row and matches
    """
    row_number = int(input(MESSAGE_ROW_NUMBER_REQUEST))
    while not check_row_number_validity(row_number, board):
        print(ERROR_NO_SUCH_ROW_OR_EMPTY_ONE)
        row_number = int(input(MESSAGE_ROW_NUMBER_REQUEST))
    amount = int(input(MESSAGE_AMOUNT_REQUEST.format(row_number)))
    while not check_amount_taken(board, row_number, amount):
        print(ERROR_ILLEGAL_AMOUNT)
        amount = int(input(MESSAGE_AMOUNT_REQUEST.format(row_number)))
    return row_number, amount


def check_row_number_validity(row_num, board):
    """
    check if the chosen row num  is valid - exist and not empty
    :return: bool- true if valid and false otherwise
    """
    return 0 <= row_num < NUM_OF_ROWS and 0 < board[row_num]


def check_amount_taken(board, row_number, amount):
    """
    check if the chosen amount is valid
    :return: bool if true in valid and false otherwise
    """
    return 0 < amount <= board[row_number]


def update_board(board, row_number, amount):
    """
    update the board after the players moves
    :param board: the game board
    :param row_number: the choosing row
    :param amount: amount of matches to remove from the choosing row
    :return: the game board after the change
    """
    board[row_number] -= amount
    return board


WINNER_MESSAGE = "The winner is.... PLAYER {} !!!!!!!!!"
TURN_MESSAGE = "Player {}, it's your turn"


def run_game():
    """
    the main func of the game
    :return: none
    """
    board = init_board()
    current_player = PLAYER_TWO
    while not is_board_empty(board):
        current_player = get_next_player(current_player)
        print(TURN_MESSAGE.format(current_player))
        print_board(board)
        row_number, amount = get_input(board)
        board = update_board(board, row_number, amount)
    print_board(board)
    print(WINNER_MESSAGE.format(current_player))


if __name__ == "__main__":
    run_game()
