import re


class WordLadderGraph:
    def __init__(self, dictionary_file):
        self.all_words = self._load_dictionary(dictionary_file)
        self.words = None
        self.word_len = None
        self.start_word = None
        self.target_word = None
        self.steps = None

    @staticmethod
    def _process_word(word):
        return word.strip()

    def _load_dictionary(self, dictionary_file):
        """
        open, and read text file and split, and get all the words
        :param dictionary_file:
        :return:
        """
        try:
            with open(dictionary_file) as data_file:
                all_words = data_file.read().splitlines()
            return list(map(self._process_word, all_words))
        except FileNotFoundError:
            print('error: %s not found' % dictionary_file)


    def _filter_dictionary(self):
        """
        Returns a reduced dictionary that only contains
        words with `word_len` characters.
        """
        length_filter = lambda word: len(word) == self.word_len
        words = filter(length_filter, self.all_words)
        if self.unwanted_word:
            not_unwanted = lambda word: word != self.unwanted_word
            words = filter(not_unwanted, words)
        return list(words)


    def _process_input_word(self, input_word):
        """
        handle the improper user input value
        :param input_word:
        :return:
        """
        try:
            word = input_word.strip()
            word_len = len(word)
            if not word_len > 0:
                raise ValueError('must not be empty')
            if not all(lambda c: c.isalpha() for c in word):
                raise ValueError('must not contain numbers')
            if input_word not in self.all_words:
                raise ValueError('must be in dictionary')
            return word
        except ValueError as ex:
            print('error: input word "%s" %s' % (input_word, str(ex)))
        exit()

    def set_start_word(self, input_word):
        """ Sets the start word """
        self.start_word = self._process_input_word(input_word)

    def set_target_word(self, input_word):
        """ Sets the target word """
        self.target_word = self._process_input_word(input_word)
        assert len(self.start_word) == len(self.target_word)
        self.word_len = len(self.target_word)

    def set_unwanted_word(self, input_vocabulary):
        """ Set the users' unwanted word """
        self.unwanted_word = input_vocabulary #self._process_input_word(input_vocabulary)
        if self.unwanted_word:
            assert len(self.start_word) == len(self.unwanted_word)

    def set_steps(self, steps):
        """ Set the user want search step number """
        self.steps = steps

    def _score(self, word):
        return (sum(s == e for (s, e) in zip(word, self.target_word))), word

    def _candidates(self, pattern, current_candidates, seen_words):
        """ Filter the words under requirements, right pattern, word seen in previous search """
        pattern_filter = lambda word: re.search(pattern, word)
        candidate_filter = lambda word: word not in current_candidates
        path_used_filter = lambda word: word not in seen_words
        return list(
            filter(path_used_filter,
                   filter(candidate_filter,
                          filter(pattern_filter, self.words)))
        )

    def _find(self, word, path, seen_words):
        """ Same as the find function in the word_ladder """
        if len(path) > self.steps + 1:
            return

        current_candidates = set()
        for i in range(self.word_len):
            if word[i] == self.target_word[i]:
                continue
            current_candidates = current_candidates | set(self._candidates(
                '%s.%s' % (word[:i], word[i + 1:]),
                current_candidates, seen_words
            ))
        seen_words = seen_words | current_candidates

        if self.target_word in current_candidates and len(path) == self.steps:
            yield len(path), path + [self.target_word]
            return

        if not len(current_candidates):
            return

        sorted_candidates = list(sorted(map(self._score, current_candidates), key=lambda x: x[0], reverse=True))

        top_score = sorted_candidates[0][0]
        if top_score == 0:
            return
        for score, cw in sorted_candidates:
            new_path = path + [cw]
            yield from self._find(cw, new_path, seen_words)
            if score != top_score:
                return

    def start(self):
        self.words = self._filter_dictionary()
        path = [self.start_word]
        seen_words = set(path)
        for path in self._find(self.start_word, path, seen_words):
            print(path)


def main():

    word_ladder = WordLadderGraph(input("Enter dictionary name: "))

    while True:
        # try:
            word_ladder.set_start_word(input("Enter start word: "))
            word_ladder.set_target_word(input("Enter target word: "))
            word_ladder.set_unwanted_word(input("Enter words you don't want to see in the path: "))
            word_ladder.set_steps(int(input("Enter steps: ")))
            word_ladder.start()

            try_again = input("Try again? [Y/n]: ")
            if not try_again.strip().lower().startswith('y'):
                break
        # except Exception as ex:
            # print(str(ex))


if __name__ == '__main__':
    main()
