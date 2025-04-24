class Solution:

    def longestWord(self, words: List[str]) -> str:

        s = set(words)
        l = max(len(w) for w in words)

        @cache
        def check(w, flag):

            if len(w) == 0:
                return True

            i = 0
            for j in range(1, len(w) + 1):
                if j - i > l:
                    return False
                if j == len(w) and flag:
                    return False
                if w[i:j] in s and check(w[j:], False):
                    return True

            return False

        words.sort(key=lambda x: (-len(x), x))
        for w in words:
            if check(w, True):
                return w

        return ""
