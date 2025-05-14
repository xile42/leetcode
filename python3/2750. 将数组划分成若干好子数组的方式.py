class Solution:

    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        base = 10 ** 9 + 7
        found = False
        pre = None
        ans = 1
        for c, ite in groupby(nums):
            if c == 0:
                if found:
                    pre = len(list(ite)) + 1
            else:
                found = True
                if pre is not None:
                    ans *= pre
                    ans %= base

        return ans % base if found else 0
