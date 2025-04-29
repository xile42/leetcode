class Solution:

    def minOperations(self, n: int) -> int:

        if n & 1:
            return ((n // 2 + 1) * 2 * (n // 2)) // 2
        else:
            return (((n // 2) * 2) * (n // 2)) // 2
