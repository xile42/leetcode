class Solution:

    def minImpossibleOR(self, nums: List[int]) -> int:

        s = set(nums)
        i = 0
        while True:
            if 2 ** i not in s:
                return 2 ** i
            i += 1
