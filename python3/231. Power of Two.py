class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        return False if n < 0 else sum([int(i) for i in bin(n)[2:]]) == 1
