def is_valid_path(board, path, words):
    """"
    :param: board
    :param: path - list of tuples
    :param: words - list of words
    :return: the word or None
    the function checks if the path that was given is valid by checking
    if the length is valid and the word is in the list word, if not the
    function return None otherwise - return the word
    """
    sorted_words = sorted(words)
    word = ''
    if len(path) == 0:
        return
    prev_cor = path[0]
    if len(path) == len(set(path)):
        for cor in path:
            if 0 <= cor[0] < len(board) and 0 <= cor[1] < len(
                    board[0]) and __if_neighbors(prev_cor, cor):
                word += board[cor[0]][cor[1]]
                prev_cor = cor
            else:
                return

    if binary_search(sorted_words, word, lambda x, y: x == y):
        return word


def binary_search(words, word, func_comp):
    """
    the function do a binary search to look for the word in the list of the
    words
    :param words: a list of words that parts can be found on the board
    :param word: a specific word to look if it in the list
    :param func_comp: a function
    :return: True if the word was found exactly in the middle False otherwise
    """
    r = len(words) - 1
    l = 0
    while l <= r:
        mid = (l + r) // 2
        if func_comp(words[mid], word):
            return True
        elif word < words[mid]:
            r = mid - 1
        elif word > words[mid]:
            l = mid + 1
    return False


def __if_neighbors(prev_cor, new_cor):
    """"
    :param: prev_cor - the current coordinate
    :param: new_cor - the next cor to checks if it near the current cor and if
    it is valid cor
    :return: True - if the next cor are valid. False - if it not
    the function checks if all the neighbors of the cell are valid
    """
    if abs(new_cor[0] - prev_cor[0]) <= 1 and abs(
            new_cor[1] - prev_cor[1]) <= 1:
        return True
    return False


def __neighbors(cor, lst_tuples, already_visited):
    """"
    :param: cor - tuple of coordinates
    :param: lst_tuple - all the coordinates of the board
    :param: already_visited - list of cors that already been picked
    :return: all the valid cell that can be picked
    """
    x, y = cor
    lst_of_neighbors = []
    valid_neighbors = []
    lst_of_neighbors += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                         (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1),
                         (x + 1, y + 1)]
    for coordinate in lst_of_neighbors:
        if coordinate in lst_tuples and coordinate not in already_visited:
            valid_neighbors.append(coordinate)
    return valid_neighbors


def is_valid_prefix(board, path, words):
    """
    the function checks if the path that was given is valid and also checks
    if the prefix of the giving word is matching to other words in the list
    :param board:
    :param path:
    :param words:
    """
    word = ''
    if len(path) == 0:
        return None
    prev_cor = path[0]
    if len(path) == len(set(path)):
        for cor in path:
            if 0 <= cor[0] < len(board[0]) and 0 <= cor[1] < len(
                    board[0]) and __if_neighbors(prev_cor, cor):
                word += board[cor[0]][cor[1]]
                prev_cor = cor
            else:
                return None

    return binary_search(words, word, lambda x, y: x.startswith(y))


def find_length_n_paths_internal(n, board, words, to_sort=True):
    """
    the function return all the paths that are at length n and sorting the
    list of the word
    :param n: an integer number that represent a length
    :param board:
    :param words: list of words
    :param to_sort: a flag represents if the list word if sorted
    :return: list of all the paths that there length is n
    """
    sorted_words = words if not to_sort else sorted(words)
    lst_of_paths = []
    path = []
    lst_tuples = __create_tuples(board)
    already_visited = []
    for cor in lst_tuples:
        already_visited.append(cor)
        __collect_path(n - 1, board, lst_of_paths, path + [cor], cor,
                       sorted_words,
                       lst_tuples, already_visited)
        already_visited.remove(cor)
    return lst_of_paths


def find_length_n_paths(n, board, words):
    """""
    :return: list of paths that in length n
    """
    return find_length_n_paths_internal(n, board, words)


def __collect_path(n, board, lst_of_paths, path, cor, sorted_words, lst_tuples,
                   already_visited, by_letter=False):
    """"
    the function iterate recursively on every letter on the board
    """
    if not is_valid_prefix(board, path, sorted_words):
        return

    if n == 0:
        if is_valid_path(board, path, sorted_words):
            lst_of_paths.append(path)
    elif n > 0:
        for neighbor in __neighbors(cor, lst_tuples, already_visited):
            size_of_letter = 1  # according length of path- every cell count as
            # one "letter" even if it has more than one
            if by_letter:
                size_of_letter = len((board[neighbor[0]][neighbor[1]]))
            already_visited.append(neighbor)
            __collect_path(n - size_of_letter, board, lst_of_paths,
                           path + [neighbor], neighbor, sorted_words,
                           lst_tuples, already_visited, by_letter)
            already_visited.remove(neighbor)


def __create_tuples(board):
    """"
    :param: board
    the function create return list of tuples that are the coordinate of
    the board
    """
    lst_of_tuple = []
    for x in range(len(board)):
        for y in range(len(board)):
            lst_of_tuple.append((x, y))
    return lst_of_tuple


def find_length_n_words(n, board, words):
    """"
    :param: n - integer number represent the required length
    :param: board
    :param: words
    :return: list of all the paths that there length is n
    the function is iterate all over the coors on the board and return the
    paths for words that there length is n
    """
    sorted_words = sorted(words)
    path = []
    lst_of_paths = []
    lst_tuples = __create_tuples(board)
    already_visited = []
    for cor in lst_tuples:
        already_visited.append(cor)
        size_of_letter = len((board[cor[0]][cor[1]]))
        __collect_path(n - size_of_letter, board, lst_of_paths, path + [cor],
                       cor, sorted_words, lst_tuples, already_visited, True)
        already_visited.remove(cor)
    return lst_of_paths


def max_score_paths(board, words):
    """"
    :param: board
    :param: words
    return: list of paths that gives the max score
    the function check what are the longest paths that can give the highest
    score and return a list of them
    """
    sorted_words = sorted(words)
    lst_of_paths = []
    lst_of_words = []
    the_longest_word = len(max(words, key=len))
    for len_of_word in range(the_longest_word, 0, -1):
        paths = find_length_n_paths_internal(len_of_word, board, sorted_words,
                                             False)
        for path in paths:
            word = create_word(path, board)
            if word not in lst_of_words:
                lst_of_words.append(word)
                lst_of_paths.append(path)
    return lst_of_paths


def create_word(path, board):
    """"
    :param: path
    :param: board
    return: word
    the function gets a list of tuples of coordinates and for each coordinate
    gets the letter from that location and return the word
    """
    word = ''
    for cor in path:
        word += board[cor[0]][cor[1]]
    return word


def load_words():
    """"
    :return: word_list
    load dict of words
    """
    with open("boggle_dict.txt") as f:  # load the word_dict list
        lines = f.readlines()
        words = list(map(str. strip, lines))
    return words