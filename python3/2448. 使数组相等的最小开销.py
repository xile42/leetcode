class Solution:

    def minCost(self, nums: List[int], cost: List[int]) -> int:

        ns = sorted(zip(nums, cost))
        nums = [i[0] for i in ns]
        cost = [i[1] for i in ns]
        tar_i = (sum(cost) + 1) // 2
        for i, v in enumerate(accumulate(cost)):
            if v >= tar_i:
                tar = nums[i]
                return sum(abs(v - tar) * cost[i] for i, v in enumerate(nums))
