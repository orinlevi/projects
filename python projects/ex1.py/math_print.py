import math


#################################################################
# FILE : math.print.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: A simple program for practicing mathematical operations.
# STUDENTS I DISCUSSED THE EXERCISE WITH: pnina.
# NOTES: its my first program to write so i needed help from other students
#################################################################

def golden_ratio():
	"""the following step will calculate and print the golden ratio:"""
	print((1 + math.sqrt(5)) / 2)


def six_squared():
	"""the following step will calculate 6^2:"""
	print(math.pow(6, 2))


def hypotenuse():
	"""the following step will calculate the hypotenuse in right-angled
	triangle whose sides are 5, 12 according to Pythagorean theorem:"""
	print(math.hypot(12, 5))


def pi():
	"""the following step will print the mathematical constant
	pi=3.141592..."""
	print(math.pi)


def e():
	"""the following step will print the mathematical constant e=2.718281..."""
	print(math.e)


def squares_area():
	"""the following step will calculate and print the areas of the squares
	whose sides are from 1-10 (ascending)"""
	print(1 ** 2, 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2, 6 ** 2, 7 ** 2, 8 ** 2,
		9 ** 2, 10 ** 2)


if __name__ == '__main__':
	golden_ratio()
	six_squared()
	hypotenuse()
	pi()
	e()
	squares_area()
