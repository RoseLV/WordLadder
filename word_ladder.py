import re

# same方法return对上号的字母 越大越好，所以后面用reverse排列。
def same(item, target):
    """
    :param item: word in words
    :param target: user input target
    :return: length of the same letter on same position between item and target.
    """
    return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
    """
    :param pattern: regular expression to find out match or not
    :param words: An array has all same length words with start word
    :param seen: dictionary has the seen word as key, and True as value
    :param list: a list of tuple has same() as the first element in an reversed order, and the words as second element.
    :return: return list[] which contains the words with one letter differ from the word.
    """
    return [word for word in words
    if re.search(pattern, word) and word not in seen.keys() and word not in list]
    # re.search = match

def find(word, words, seen, target, path):
    """
    :param word: each word in the dictionary
    :param words: An array has all same length words with start word
    :param seen: dictionary has the seen word as key, and True as value
    :param target:  target word
    :param path: the path from start word to the target word
    :return: True/ False
    """
    list = []
    for i in range(len(word)):
        if word[i] != target[i]:  # this will reduce the words in list
            list += build(word[:i] + "." + word[i + 1:], words, seen, list)
            print("2")
            print(list)

    # In the loop, any step len(list)==0 means there is no path.
    if len(list) == 0:
        return False

    # In the loop, once the target is found in the list, one path is found.
    if target in list:
        return True

    # sorted in decrease order so that it is easier to choose the shortest way.
    list = sorted([(same(w, target), w) for w in list], reverse=True)


    for (match, item) in list:
        if match >= len(target) - 1:  # if not the same and there is one or more letters different.
            if match == len(target) - 1:  # only one letter differ from target，eg：len（target）=4, match=3；
                path.append(item)
            return True
        seen[item] = True

    for (match, item) in list:
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()


def get_dictionary(fileName):
    """
    :param fileName: file name, user input
    :return: each line in the file
    """
    file = open(fileName)
    lines = file.readlines()
    return lines


def start(start, lines):
    """
    :param start: start word, user input
    :param lines: each line in the file
    :return: start, words
    """
    words = []
    for line in lines:
        word = line.rstrip()
        if len(word) == len(start):
            words.append(word)

    if start not in words:
        raise ValueError(start + " is not in the dictionary, please try another one.")
    return start, words


def target(target, start, words):
    """
    :param target: target words
    :param start: start words
    :param words: word list has all the same length words as the start word in the file
    :return: target word
    """
    if len(target) != len(start) or target not in words:
        raise ValueError(target + " is not same length with start word or not in the list, please try another one.")
    return target


def find_path(start, target):
    """
    :param start: start word
    :param target: target word
    :return: path length, path/ "No path found"
    """
    path = [start]  # User input start
    seen = {start: True}  # {DICTIONARY KEY:START, VALUE:TRUE} #avoid repeated word in the list
    if find(start, words, seen, target, path):
        path.append(target)  # append target one by one 一层一层加
        print(len(path) - 1, path)
    else:
        print("No path found")


if __name__ == '__main__':

    while True:

        try:
            lines = get_dictionary(input("Enter dictionary name: "))
        except:
            print("This word is not in the dictionary, please try another one.")
            continue

        try:
            start_word, words = start(input("Enter start word: "), lines)
        except:
            print("try another one")
            continue

        try:
            target_word = target(input("Enter target word: "), start_word, words)
        except:
            print(target_word + " must have same length as start and in the dictionary, please try another one.")
            continue

        find_path(start_word, target_word)

