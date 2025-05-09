class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)

        @cache
        def f(i, tar, left):

            if i >= n:
                return tar * (k - left)

            ans = 0
            if left:
                ans = max(ans, f(i + 1, max(tar, arr[i]), left - 1))
            ans = max(ans, f(i + 1, arr[i], k - 1) + tar * (k - left))

            return ans

        return f(0, -inf, k)
