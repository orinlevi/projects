import typing as t
from ex7_helper import *


#################################################################
# FILE : ex7.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex7 2022
# DESCRIPTION: writing recursions functions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina Eisenbach.
#################################################################

def mult(x: float, y: int) -> float:
	"""
	return the multiplication of 2 numbers
	:param x: the first num
	:param y: the second num
	:return: multiplication (float)
	"""
	if y == 0 or x == 0:
		return 0
	else:
		return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
	"""
	check if gaven num is even
	:param n: number
	:return: True if num is even and False otherwise
	"""
	if n == 0:
		return True
	if n == 1:
		return False
	else:
		return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int) -> float:
	"""
	return the multiplication of 2 numbers whit shorter run time
	:param x: the first num
	:param y: the second num
	:return: multiplication (float)
	"""
	if y == 0 or x == 0:
		return 0
	if y == 1:
		return x
	partial_sum: float = log_mult(x, divide_by_2(y))
	if is_odd(y) is True:
		return add(add(partial_sum, partial_sum), x)
	else:
		return add(partial_sum, partial_sum)


def _helper_is_power(pow_b: int, x: int, original_b: int) \
	-> bool:
	"""
	Checks if small is some root of large
	:param pow_b: number
	:param x: number
	:param original_b: multiply numbers
	:return: True if small is some root of large and False otherwise
	"""
	if pow_b == x or x == 1:
		return True
	elif (pow_b > x) or (pow_b == 0) or (pow_b == 1):
		return False
	else:
		return _helper_is_power(int(log_mult(pow_b, original_b)), x, original_b)


def is_power(b: int, x: int) -> bool:
	"""
	Checks if b is some root of x
	:param b:number
	:param x:number
	:return:True if b is some root of x and False otherwise
	"""
	return _helper_is_power(b, x, b)


def _reverse_helper(string_to_reverse: str, index: int) -> str:
	"""
	return string from its end to its begin
	:param string_to_reverse: a given string
	:param index: index of specific letter in the string. start from the
	first one- 0.
	:return: string from its end to its begin
	"""
	if index == len(string_to_reverse):
		return ''
	else:
		return append_to_end(_reverse_helper(string_to_reverse, index + 1),
			string_to_reverse[index])


def reverse(s: str) -> str:
	"""
	return string from its end to its begin
	:return: string from its end to its begin
	"""
	return _reverse_helper(s, 0)


def play_hanoi(Hanoi: t.Any, n: int, src: t.Any, dst: t.Any, temp: t.Any) -> \
	None:
	"""
	run hanoi game
	"""
	if n < 0:
		n = 0
	if n == 0:
		return None
	if n > 0:
		play_hanoi(Hanoi, n - 1, src, temp, dst)
		Hanoi.move(src, dst)
		play_hanoi(Hanoi, n - 1, temp, dst, src)


def _number_of_ones_helper(n: int) -> int:
	"""
	count how many time the number "1" appear in the numbers between 1-n
	:param n: number
	:return: how many time the number "1" appear in the numbers between 1-n
	"""
	if n == 0:
		return 0
	if n % 10 == 1:
		return 1 + _number_of_ones_helper(n // 10)
	else:
		return _number_of_ones_helper(n // 10)


def number_of_ones(n: int) -> int:
	"""
	count how many time the number "1" appear in the numbers between 1-n
	:param n: number
	:return: how many time the number "1" appear in the numbers between 1-n
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return _number_of_ones_helper(n) + number_of_ones(n - 1)


def _external_list_helper(l1: t.List[t.List[int]], l2: t.List[
	t.List[int]], index: int) -> bool:
	"""
	compere between the external lists
	:param l1
	:param l2
	:param index: specific list
	:return: True if the external lists are identical and False otherwise
	"""
	if index == len(l1) and index == len(l2):
		return True
	elif (index != len(l1) and index == len(l2)) or (index == len(l1) and
	                                               index != len(l2)):
		return False
	return _internal_list_helper(l1[index], l2[index], 0) and \
	       _external_list_helper(l1, l2, index + 1)


def _internal_list_helper(l1: t.List[int], l2: t.List[int], index: int) -> \
	bool:
	"""
	compere between the internal lists
	:param l1
	:param l2
	:param index: specific internal list
	:return: True if the internal lists are identical and False otherwise
	"""
	if index == len(l1) and index == len(l2):
		return True
	if (index != len(l1) and index == len(l2)) or (index == len(l1) and
	                                               index != len(l2)):
		return False
	return l1[index] == l2[index] and _internal_list_helper(l1, l2, index + 1)


def compare_2d_lists(l1: t.List[t.List[int]], l2: t.List[t.List[int]]) -> bool:
	"""
	Compares two lists and checks if they are identical
	:param l1
	:param l2
	:return: True if the lists are identical and False otherwise
	"""
	return _external_list_helper(l1, l2, 0)


def magic_list(n: int) -> t.List[t.Any]:
	"""
	Returns a list with n object and and each of them contains the previous
	ones
	:param n: the the length of the list
	:return: a list with n object and and each of them contains the previous
	"""
	if n == 0:
		return []
	else:
		lst = magic_list(n - 1)
		lst.append(magic_list(n - 1))
		return lst

if __name__ == '__main__':
	print(reverse('')
)
