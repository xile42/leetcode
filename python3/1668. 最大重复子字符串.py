class Solution:

    def maxRepeating(self, sequence: str, word: str) -> int:

        n = len(sequence) // len(word)
        for i in range(n, -1, -1):
            if word * i in sequence:
                return i
