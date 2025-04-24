class Solution:

    def makeEqual(self, words: List[str]) -> bool:

        n = len(words)

        c = Counter()
        for w in words:
            c += Counter(w)

        for v in c.values():
            if v % n != 0:
                return False

        return True
