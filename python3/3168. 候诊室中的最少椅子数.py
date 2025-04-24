class Solution:

    def minimumChairs(self, s: str) -> int:

        n = [1 if c == "E" else -1 for c in s]

        return max(accumulate(n))
