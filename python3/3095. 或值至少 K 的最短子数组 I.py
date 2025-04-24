class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        res_all = reduce(or_, nums)
        if res_all < k:
            return -1

        for l in range(1, len(nums) + 1):
            for i in range(len(nums) - l + 1):
                res = reduce(or_, nums[i:i+l])
                if res >= k:
                    return l
