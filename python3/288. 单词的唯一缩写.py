class ValidWordAbbr:

    def f(self, s):

        return s if len(s) <= 2 else s[0] + str(len(s) - 2) + s[-1]

    def __init__(self, dictionary: List[str]):

        self.d = defaultdict(set)
        for w in dictionary:
            self.d[self.f(w)].add(w)

    def isUnique(self, word: str) -> bool:

        sw = self.f(word)
        if sw not in self.d:
            return True

        if len(self.d[sw]) == 1 and word in self.d[sw]:
            return True

        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)