class Solution:

    def canPermutePalindrome(self, s: str) -> bool:

        c = Counter(s)

        return sum(v & 1 == 1 for v in c.values()) <= 1
