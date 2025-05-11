class Solution:

    def totalMoney(self, n: int) -> int:
        i = n // 7
        j = n - i * 7
        ans = 0
        ans += 7 * (i + 1) * i // 2 + 6 * (6 + 1) // 2 * i
        for n in range(i + 1, i + 1 + j):
            ans += n

        return ans
