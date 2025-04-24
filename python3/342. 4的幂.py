class Solution:

    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0 or (n & (n-1)) != 0:
            return False

        x = len(bin(n)[2:]) - 1
        if x & 1:
            return False

        return True
        
