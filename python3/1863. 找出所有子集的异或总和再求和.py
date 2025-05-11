class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:

        ans = 0
        for l in range(1, len(nums) + 1):
            for arr in combinations(nums, l):
                ans += reduce(xor, arr)

        return ans