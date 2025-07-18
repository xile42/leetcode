class Solution:

    def validPartition(self, nums: List[int]) -> bool:

        def check(ns):

            return (len(ns) == 2 and ns[0] == ns[1]) or (len(ns) == 3 and ns[0] == ns[1] and ns[1] == ns[2]) or (len(ns) == 3 and ns[0] == ns[1] - 1 and ns[1] == ns[2] - 1)

        @cache
        def f(i):

            if i >= len(nums):
                return True

            for j in [i + 2, i + 3]:
                if check(nums[i:j]) and f(j):
                    return True

            return False

        return f(0)
