import re


class Solution:

    def numDifferentIntegers(self, word: str) -> int:

        s = re.sub("[^\d]", " ", word)
        v = re.split("\s+", s)
        v = set([int(i) for i in v if len(i)])

        return len(v)
