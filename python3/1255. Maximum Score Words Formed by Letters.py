class Solution:

    result = None

    def check(self, word, counter):

        new_counter = dict()
        new_counter.update(counter)
        for char in word:
            if char not in new_counter or new_counter[char] == 0:
                return False, dict()
            new_counter[char] -= 1

        return True, new_counter

    def search(self, words, word_scores, score, counter_left):

        if len(words) == 0:
            self.result = max(self.result, score)
            return

        check_result, new_counter = self.check(words[0], counter_left)

        self.search(
            [] if len(words) == 1 else words[1:],
            [] if len(word_scores) == 1 else word_scores[1:],
            score,
            counter_left)

        if check_result:
            self.search(
                [] if len(words) == 1 else words[1:],
                [] if len(word_scores) == 1 else word_scores[1:],
                score+word_scores[0],
                new_counter)

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        from collections import Counter
        from string import ascii_lowercase

        idx_map = {char: idx for idx, char in enumerate(list(ascii_lowercase))}
        counter_all = Counter(letters)
        valid_words = list()
        valid_scores = list()

        for word in words:
            counter = Counter(word)
            valid = True
            word_score = 0
            for k, v in counter.items():
                word_score += score[idx_map[k]] * v
                if k not in counter_all or counter_all[k] < v:
                    valid = False
                    break
            if valid:
                valid_scores.append(word_score)
                valid_words.append(word)

        self.result = 0
        self.search(valid_words, valid_scores, 0, counter_all)

        return self.result
