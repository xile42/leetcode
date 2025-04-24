class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:

        ans = comb(10, n) * factorial(n)

        ans = 1
        for i in range(1, n + 1):
            if i == 1:
                ans += 9
            else:
                cur = 9
                for j in range(i - 1):
                    cur *= 9 - j
                ans += cur

        return ans
