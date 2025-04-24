class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def f(n):

            if n == 0:
                return 1

            result = 0
            for i in nums:
                if n - i >= 0:
                    result += f(n-i)

            return result

        return f(target)
