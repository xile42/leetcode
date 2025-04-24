class Solution:

    def maximumProduct(self, nums: List[int]) -> int:

        sn = sorted(nums)

        return max(reduce(mul, sn[-3:]), reduce(mul, sn[:2] + [sn[-1]]))
