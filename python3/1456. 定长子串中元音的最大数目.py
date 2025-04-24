class Solution:

    def maxVowels(self, s: str, k: int) -> int:

        ns = [1 if c in "aeiou" else 0 for c in s]
        acc = [0] + list(accumulate(ns))
        ans = 0
        for i in range(k - 1, len(s)):
            ans = max(ans, acc[i + 1] - acc[i - k + 1])

        return ans
