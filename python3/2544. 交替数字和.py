class Solution:

    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        s = 1
        for c in map(int, str(n)):
            ans += c * s
            s *= -1

        return ans