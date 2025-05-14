class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            ans += n % 2 == 0 and sum(map(int, s[:n // 2])) == sum(map(int, s[- n // 2:]))

        return ans