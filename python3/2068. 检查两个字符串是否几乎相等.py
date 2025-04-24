class Solution:

    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        c1, c2 = Counter(word1), Counter(word2)

        return all(i <= 3 for i in (c1 - c2).values()) and all(i <= 3 for i in (c2 - c1).values())
