class Solution:

    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:

        c = Counter()
        n = len(word)
        for i in range(n // k):
            c[word[i * k:(i + 1) * k]] += 1

        return n // k - max(c.values())
