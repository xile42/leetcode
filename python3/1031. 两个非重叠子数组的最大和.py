class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

        n = len(nums)
        acc = list(accumulate(nums))
        la, lb = firstLen, secondLen

        def f(la, lb):

            ans = -inf
            left_value = -inf
            for i in range(la, n - lb + 1):
                right_value = acc[i + lb - 1] - acc[i - 1]
                left_value = max(left_value, acc[i - 1] - (0 if i - 1 - la < 0 else acc[i - 1 - la]))
                ans = max(ans, left_value + right_value)

            return ans

        return max(f(la, lb), f(lb, la))
