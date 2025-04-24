class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:

        ans = -inf
        mi = max(nums[0], nums[1])
        ij = nums[0] - nums[1]
        for v in nums[2:]:
            ans = max(ans, ij * v)
            ij = max(ij, mi - v)
            mi = max(mi, v)

        return 0 if ans < 0 else ans
