class Solution:

    def checkPerfectNumber(self, num: int) -> bool:

        ans = -num
        for i in range(1, isqrt(num) + 1):
            if num % i == 0:
                ans += i
                if i * i != num:
                    ans += num // i

        return ans == num