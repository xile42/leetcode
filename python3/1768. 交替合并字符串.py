class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        l1, l2 = len(word1), len(word2)
        l = min(l1, l2)

        return "".join([i + j for i, j in zip(word1, word2)]) + word1[l:] + word2[l:]
