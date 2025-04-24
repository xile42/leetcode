class Solution:

    def countQuadruplets(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        hashmap = defaultdict(int)
        for c, x in enumerate(nums):
            for d in range(c + 1, n):
                ans += hashmap[nums[d] - x]
            for a in range(c):
                hashmap[nums[a] + x] += 1

        return ans
