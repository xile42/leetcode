class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:

        ans = 0
        mx = -inf
        n = len(nums)

        def f(i, cur):

            nonlocal ans, mx
            if i >= n:
                if cur > mx:
                    mx = cur
                    ans = 1
                elif cur == mx:
                    ans += 1
                return

            f(i + 1, cur | nums[i])
            f(i + 1, cur)

        f(0, 0)

        return ans
