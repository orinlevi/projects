#################################################################
# FILE : ex3.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex3 2021
# DESCRIPTION: practice of using loops and variables.
# STUDENTS I DISCUSSED THE EXERCISE WITH: Pnina Eisenbach.
#################################################################


"""the function receives input of numbers from the user as a string and returns
a list that contains the numbers as floats and their sum"""


def input_list():
	input_num_list = []
	input_sum = 0
	num_from_user = input()
	while len(num_from_user) != 0:
		input_num_list.append(float(num_from_user))
		num_from_user = input()
	for i in input_num_list:
		input_sum += i
	input_num_list.append(input_sum)
	return input_num_list


"""the function receives two vectors (list of numbers) and returns their
inner product"""


def inner_product(vec_1, vec_2):
	inner_product_space = 0
	if len(vec_1) == len(vec_2):
		for i in range(len(vec_1)):
			inner_product_space += vec_1[i] * vec_2[i]
		return inner_product_space
	else:
		return None


"""the function receives a series (list of numbers) and classifies it as
increasing, strictly increasing, decreasing and strictly decreasing"""


def sequence_monotonicity(sequence):
	increasing = True
	strictly_increasing = True
	decreasing = True
	strictly_decreasing = True
	for i in range(1, len(sequence)):
		if (sequence[i - 1] <= sequence[i]) is not True:
			increasing = False
			break
	for i in range(1, len(sequence)):
		if (sequence[i - 1] < sequence[i]) is not True:
			strictly_increasing = False
			break
	for i in range(1, len(sequence)):
		if (sequence[i - 1] >= sequence[i]) is not True:
			decreasing = False
			break
	for i in range(1, len(sequence)):
		if (sequence[i - 1] > sequence[i]) is not True:
			strictly_decreasing = False
			break
	return [increasing, strictly_increasing, decreasing, strictly_decreasing]


"""the function receives characteristics of series of numbers (increasing,
strictly increasing, decreasing and strictly decreasing) and provides an
example for each combination of characteristics """


def monotonicity_inverse(def_bool):
	increasing = def_bool[0]
	strictly_increasing = def_bool[1]
	decreasing = def_bool[2]
	strictly_decreasing = def_bool[3]
	strictly_increasing_series_example = [1, 2, 3, 4]
	increasing_series_example = [1, 1, 2, 3]
	permanent_series_example = [1, 1, 1, 1]
	decreasing_series_example = [4, 3, 2, 2]
	strictly_decreasing_series_example = [4, 3, 2, 1]
	not_increasing_or_decreasing_series_example = [1, 3, 2, -1]
	if increasing is True:
		if strictly_increasing is True:
			if decreasing is False and strictly_decreasing is False:
				return strictly_increasing_series_example
			else:
				return None
		elif decreasing is True:
			if strictly_decreasing is False:
				return permanent_series_example
			else:
				return None
		elif strictly_decreasing is False:
			return increasing_series_example
		else:
			return None
	elif decreasing is True:
		if strictly_decreasing is True:
			if strictly_increasing is False:
				return strictly_decreasing_series_example
			else:
				return None
		elif strictly_increasing is False:
			return decreasing_series_example
		else:
			return None
	elif strictly_increasing is False and strictly_decreasing is False:
		return not_increasing_or_decreasing_series_example
	else:
		return None


"""the function receives a number (n) and returns the 'n' first primes
numbers"""


def primes_for_asafi(n):
	prime_numbers = []
	num = 2
	while num > 1 and n > len(prime_numbers):
		for divisor in range(2, int(num**0.5)+1):
			if num % divisor == 0:
				break
		else:
			prime_numbers.append(num)
		num += 1
	return prime_numbers


"""the function receives multiple vectors and returns their sum"""


def sum_of_vectors(vec_lst):
	if vec_lst == []:
		return None
	elif vec_lst == [[]] * len(vec_lst):
		return []
	else:
		vectors_sum = [0] * len(vec_lst[0])
		for j in range(len(vec_lst)):
			for i in range(len(vec_lst[0])):
				vectors_sum[i] += vec_lst[j][i]
	return vectors_sum


"""the function receives multiple vectors and returns the amount of the
pairs that orthogonal to each other"""


def num_of_orthogonal(vectors):
	num_of_orthogonal_pairs = 0
	for i in range(len(vectors)):
		for j in range(len(vectors)):
			if j != i:
				if inner_product(vectors[i], vectors[j]) == 0:
					num_of_orthogonal_pairs += 1
	num_of_orthogonal_pairs /= 2
	return int(num_of_orthogonal_pairs)
