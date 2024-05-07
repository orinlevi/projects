from typing import List, Tuple, Set, Optional
from copy import deepcopy


#################################################################
# FILE : ex8.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex8 2022
# DESCRIPTION: in this exercise I will implement a solution to the logic
# puzzle (game) using backtracking.
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina.
#################################################################


# We define the types of a partial picture and a constraint (for type checking)
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def _seen_cells_helper(picture: List[List[int]], row: int, col: int,
                       stop: int) -> int:
	"""
	checks the cells to the right, left, top and bottom of the given cell
	and counts how many cells are visible from it including itself depending on the given
	conditions ((-1) is considered white or black)
	:param picture: a given partial picture
	:param row: the row of the cell
	:param col: the column of the cell
	:param stop: -1 or 0 depend if (-1) is considered white or black (min or max).
	If during the counting of the seen cells its encounter a cell that
	is considered black (-1 or 0 depending on the conditions) its stop counting
	because the "black" cell hides the other cells that follow it in
	relation to the given cell.
	:return: how many cells are visible from the given cell including itself.
	"""
	if picture[row][col] == 0 or picture[row][col] == stop:
		return 0
	else:
		_max_seen_cells = 1  # count the cell itself
		for _right in range(col + 1, len(picture[row])):
			if picture[row][_right] != stop and picture[row][_right] != 0:
				_max_seen_cells += 1
			else:
				break
		for _left in range(col - 1, -1, -1):
			if picture[row][_left] != stop and picture[row][_left] != 0:
				_max_seen_cells += 1
			else:
				break
		for _down in range(row + 1, len(picture)):
			if picture[_down][col] != stop and picture[_down][col] != 0:
				_max_seen_cells += 1
			else:
				break
		for _up in range(row - 1, -1, -1):
			if picture[_up][col] != stop and picture[_up][col] != 0:
				_max_seen_cells += 1
			else:
				break
	return _max_seen_cells


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
	"""
	checks the cells to the right, left, top and bottom of the given cell
	and check the max cells that are visible from it including itself.
	in this function only "(0) cell" considered black.
	:param picture: a given partial picture
	:param row: the row of the cell
	:param col: the column of the cell
	:return: the max cells that are visible from the given cell including
	itself
	"""
	return _seen_cells_helper(picture, row, col, 0)


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
	"""
	checks the cells to the right, left, top and bottom of the given cell
	and check the min cells that are visible from it including itself.
	in this function "(-1) and (0) cell" considered black.
	:param picture: a given partial picture
	:param row: the row of the cell
	:param col: the column of the cell
	:return: the min cells that are visible from the given cell including
	itself
	"""
	return _seen_cells_helper(picture, row, col, -1)


def check_constraints(picture: Picture, constraints_set: Set[
	Constraint]) -> int:
	"""
	the function return an integer between 0 and 2 that indicates success
	Satisfying the given constraints in the partial picture.
	:param picture: a given partial picture
	:param constraints_set: given constraints that are supposed to exist in
	the board.
	set structure- (row of the cell, col of the cell, seen-how many cells
	supposed to seen from the
	cell)
	:return: an integer between 0 and 2 that indicates success Satisfying
	the constraints in the partial picture.
	"""
	x = 1
	for constraint in constraints_set:
		row = constraint[0]
		col = constraint[1]
		con_seen = constraint[2]
		if min_seen_cells(picture, row, col) == max_seen_cells(picture, row,
			col) == con_seen:
			continue
		elif min_seen_cells(picture, row, col) <= con_seen <= \
			max_seen_cells(picture, row, col):
			x = 2
		else:
			return 0
	return x


def _solve_puzzle_helper(constraints_set: Set[Tuple[int, int, int]], n: int,
                         m: int, pic: List[List[int]], ind: int = 0) -> \
	Optional[List[List[int]]]:
	"""
	the function implements and returns a single solution to the game.
	:param constraints_set: given constraints that are supposed to exist in
	the board.
	:param n: num of rows in the game board
	:param m: num of columns in the game board
	:param pic: a given empty picture- all cells values are equal to (-1).
	:param ind: num of cell in the board game. there are n x m cells.
	:return: a single solution to the game
	"""
	if ind == n * m:
		return pic
	row, col = ind // m, ind % m
	for value in [0, 1]:
	# for value in range(2):
		pic[row][col] = value
		if check_constraints(pic, constraints_set) != 0:
			pic_solution = _solve_puzzle_helper(constraints_set, n, m, pic,
				ind + 1)
			if pic_solution:
				return pic_solution
		# if check_constraints(pic, constraints_set) == 1:
		# 	for row in pic:
		# 		if -1 in row:
		# 			_solve_puzzle_helper(constraints_set, n, m, pic, ind + 1)
		# 	return pic
	pic[row][col] = -1

		# if check_constraints(pic, constraints_set) == 2:
		# 	pic[row][col] = value
		# 	solution = _solve_puzzle_helper(constraints_set, n, m, pic, ind + 1)
		# 	if check_constraints(pic, constraints_set) == 1:
		# 		return solution
		# pic[row][col] = -1


# def _solve_puzzle_helper(constraints_set: Set[Tuple[int, int, int]], n: int,
#                          m: int, pic: List[List[int]], solution: List,
#                          ind: int = 0) -> \
# 	Optional[List[List[int]]]:
# 	"""
# 	the function implements and returns a single solution to the game.
# 	:param constraints_set: given constraints that are supposed to exist in
# 	the board.
# 	:param n: num of rows in the game board
# 	:param m: num of columns in the game board
# 	:param pic: a given empty picture- all cells values are equal to (-1).
# 	:param ind: num of cell in the board game. there are n x m cells.
# 	:return: a single solution to the game
# 	"""
# 	if ind == n * m:
# 		solution.append(deepcopy(pic))
# 		return
# 	row, col = ind // m, ind % m
# 	for value in [0, 1]:
# 		pic[row][col] = value
# 		if check_constraints(pic, constraints_set) != 0:
# 			_solve_puzzle_helper(constraints_set, n, m, pic, solution, ind + 1)
# 	pic[row][col] = -1
# 	if len(solution) != 0:
# 		return solution[0]
# 	else:
# 		return
#################################################################
# FILE : puzzle_solver.py
# WRITER : omer reuven , omer.reuven2 , 207659764
# EXERCISE :  ex8 backtracking
# DESCRIPTION: solution to the logic
#  puzzle (game) using backtracking.
# STUDENTS I DISCUSSED THE EXERCISE WITH: orin levi
#################################################################

def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[
	Picture]:
	"""
	he function implements and returns a single solution to the game.
	:param constraints_set: given constraints that are supposed to exist in
	the board.
	:param n: num of rows in the game board
	:param m: num of columns in the game board
	:return: a single solution to the game
	"""
	picture = [[-1] * m for _ in range(n)]  # creates an empty picture- all
	# cells values are equal to (-1)
	return _solve_puzzle_helper(constraints_set, n, m, picture)


def _how_many_helper(constraints_set: Set[Tuple[int, int, int]], n: int,
                     m: int, pic: List[List[int]], ind: int = 0, counter:
	int = 0) -> int:
	"""
	the function counts and returns the the number of all the possible
	solutions for the game.
	:param constraints_set: given constraints that are supposed to exist in
	the board.
	:param n: num of rows in the game board
	:param m: num of columns in the game board
	:param pic: a given empty picture- all cells values are equal to (-1).
	:param ind: num of cell in the board game. there are nxm cells.
	:param counter: count how many solutions the game has.
	:return: the the number of all the possible
	solutions for the game
	"""
	if ind == n * m:
		return 1
	row, col = ind // m, ind % m
	for value in [0, 1]:
	# for value in range(2):
		pic[row][col] = value
		if check_constraints(pic, constraints_set) != 0:
			counter += _how_many_helper(constraints_set, n, m, pic, ind + 1)
	pic[row][col] = -1
	return counter


def how_many_solutions(constraints_set: Set[
	Constraint], n: int, m: int) -> int:
	"""
	the function counts and returns the the number of all the possible
	solutions for the game.
	:param constraints_set: given constraints that are supposed to exist in
	the board.
	:param n: num of rows in the game board
	:param m: num of columns in the game board
	:return: the the number of all the possible
	solutions for the game
	"""
	picture = [[-1] * m for _ in range(n)]  # creates an empty picture- all
	# cells values are equal to (-1)
	return _how_many_helper(constraints_set, n, m, picture)


def _helper_generate_puzzle(pic: Picture, n: int, m: int) -> set[Constraint]:
	"""

	:param pic:
	:param n:
	:param m:
	:return:
	"""
	constraints = []
	for cell in range(n * m):
		row, col = cell // m, cell % m
		constraints.append((cell // m, cell % m, max_seen_cells(pic, cell // m, cell % m)))
	for con in set(constraints):
		constraints.remove(con)
		if how_many_solutions(set(constraints), n, m) == 1:
			continue
		else:
			constraints.append(con)
	return set(constraints)


def generate_puzzle(picture: Picture) -> Set[Constraint]:
	"""

	:param picture:
	:return:
	"""
	n = len(picture)
	m = len(picture[0])
	return _helper_generate_puzzle(picture, n, m)

if __name__ == '__main__':
	s = solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4)
	print(s)
#           == [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]



