import hangman_helper

#################################################################
# FILE : hangman.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex4 2021
# DESCRIPTION: programing a "hang man" game
# STUDENTS I DISCUSSED THE EXERCISE WITH: Meir Wolitsky
#################################################################


def update_word_pattern(word, pattern, letter):
	"""

	:param word:
	:param pattern:
	:param letter:
	:return:
	"""
	new_pattern = pattern
	for i in range(len(word)):
		if word[i] == letter:
			new_pattern = new_pattern[:i] + letter + new_pattern[i + 1:]
	return new_pattern


def checker_letters(letter_guess, guesses_list, word):
	"""

	:param letter_guess:
	:param guesses_list:
	:param word:
	:return:
	"""
	msg = ""
	correct_letter = None
	if len(letter_guess) == 1 and letter_guess == str.lower(letter_guess) \
		and letter_guess.isalpha():
		if letter_guess not in guesses_list:
			if letter_guess in word:
				correct_letter = True
				msg = "correct"
			else:
				correct_letter = False
				msg = "wrong_guess"
		else:
			msg = "you have already chose this letter"
	else:
		msg = "you can only type a a-z letter (in lowercase letters)"
	return msg, correct_letter


def checker_words(word_guess, word):
	"""

	:param word_guess:
	:param word:
	:return:
	"""
	msg = ""
	correct_word = None
	if len(word_guess) == len(word) and word_guess == str.lower(word_guess) \
		and word_guess.isalpha():
		if word_guess == word:
			correct_word = True
			msg = "correct word, you won"
	return msg, correct_word


def amount_of_repeats(letter, word):
	"""

	:param letter:
	:param word:
	:return:
	"""
	counter_repeats = 0
	for lett in word:
		if lett == letter:
			counter_repeats += 1
	return counter_repeats


def run_single_game(word_list, score):
	"""

	:param word_list:
	:param score:
	:return:
	"""
	word = hangman_helper.get_random_word(word_list)
	pattern = "_" * len(word)
	wrong_guess_lst = []
	points = score
	msg = "good luck"
	whole_guesses = []
	underscore_in_pattern = len(word)
	while points != 0 and underscore_in_pattern != 0:
		hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)
		gamer_input = hangman_helper.get_input()
		type_of_input = gamer_input[0]
		guess_input = gamer_input[1]
		if type_of_input == hangman_helper.HINT:
			points -= 1
			filtered_list_for_hint = filter_words_list(word_list, pattern, wrong_guess_lst)
			hangman_helper.show_suggestions(filtered_list_for_hint)
		elif type_of_input == hangman_helper.WORD:
			parm_w = checker_words(guess_input, word)
			message_w = parm_w[0]
			correct_word = parm_w[1]
			msg = message_w
			points -= 1
			if correct_word is True:
				u = underscore_in_pattern
				points += ((u * (u + 1)) // 2) 
				pattern = word
				underscore_in_pattern = 0
		elif type_of_input == hangman_helper.LETTER:
			parm_l = checker_letters(guess_input, whole_guesses, word)
			message_l = parm_l[0]
			correct_letter = parm_l[1]
			msg = message_l
			if correct_letter is False:
				points -= 1
				wrong_guess_lst.append(guess_input)
			elif correct_letter is True:
				pattern = update_word_pattern(word, pattern, guess_input)
				r = amount_of_repeats(guess_input, word)
				points += ((r * (r + 1)) // 2) - 1
				underscore_in_pattern -= r
		if underscore_in_pattern == 0:
			msg = "you won"
		if points == 0:
			msg = "game over, the word was " + word
		whole_guesses.append(guess_input)
	hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)
	return points


def main():
	"""

	:return:
	"""
	word_list = hangman_helper.load_words()
	points = hangman_helper.POINTS_INITIAL
	num_of_games = 0
	question_msg = ""
	while True:
		score = run_single_game(word_list, points)
		points = score
		num_of_games += 1
		if score != 0:
			question_msg = "you have earned so far " + str(points) + " " \
			"points and played " + str(num_of_games) + " games.\ndo you " \
			                                            "want to keep playing?"
			player_answer = hangman_helper.play_again(question_msg)
			if player_answer is False:
				break
		else:
			question_msg = "you have earned so far " + str(points) + " " \
			"points and played " + str(num_of_games) + " games.\ndo you " \
			                                            "want to play again?"
			player_answer = hangman_helper.play_again(question_msg)
			if player_answer is True:
				num_of_games = 0
				points = hangman_helper.POINTS_INITIAL
			else:
				break


def initial_word_filter(words_lst, wrong_letters, pattern):
	"""

	:param words_lst:
	:param wrong_letters:
	:param pattern:
	:return:
	"""
	initial_filtered_words = []
	for word in words_lst:
		if len(word) == len(pattern):
			for letter in wrong_letters:
				if letter in word:
					break
			else:
				initial_filtered_words.append(word)
	return initial_filtered_words


def second_filter(first_filtered_word_list, pattern):
	"""

	:param first_filtered_word_list:
	:param pattern:
	:return:
	"""
	second_filtered_words = []
	for word in first_filtered_word_list:
		for i in range(len(pattern)):
			if pattern[i].isalpha():
				if word[i] != pattern[i] or pattern.count(pattern[i]) != \
					word.count(pattern[i]):
					break
		else:
				second_filtered_words.append(word)
	return second_filtered_words


def final_filter_lst(second_filtered_words):
	"""

	:param second_filtered_words:
	:return:
	"""
	final_word_list_for_hint = []
	n = len(second_filtered_words)
	if len(second_filtered_words) > hangman_helper.HINT_LENGTH:
		for i in range(hangman_helper.HINT_LENGTH):
			s_f_index = (i * n) // hangman_helper.HINT_LENGTH
			final_word_list_for_hint.append(second_filtered_words[s_f_index])
	else:
		final_word_list_for_hint = second_filtered_words
	return final_word_list_for_hint


def filter_words_list(words, pattern, wrong_guess_lst):
	"""

	:param words:
	:param pattern:
	:param wrong_guess_lst:
	:return:
	"""
	first_filtered_list = initial_word_filter(words, wrong_guess_lst, pattern)
	second_filtered_list = second_filter(first_filtered_list, pattern)
	filtered_list_for_hint = final_filter_lst(second_filtered_list)
	return filtered_list_for_hint
