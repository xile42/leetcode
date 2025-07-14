class Solution:

    def preimageSizeFZF(self, k: int) -> int:

        def check(n):

            ans = 0
            while n:
                n //= 5
                ans += n

            return ans

        def f(x):

            left = 0
            right = 5 * (x + 1)
            while left <= right:
                mid = (left + right) // 2
                v = check(mid)
                if v > x:
                    right = mid - 1
                else:
                    left = mid + 1

            return right

        return f(k) - f(k - 1)
