class Solution:

    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:

        def f(a, b):

            res = 0
            for ai, bi in zip(a, b):
                res += abs(ai - bi)

            return res

        ans1 = f(arr, brr)
        ans2 = f(sorted(arr), sorted(brr)) + k

        return min(ans1, ans2)
