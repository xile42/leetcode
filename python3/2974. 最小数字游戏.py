class Solution:

    def numberGame(self, nums: List[int]) -> List[int]:

        sn = sorted(nums)

        return reduce(add, [sn[i:i+2][::-1] for i in range(0, len(sn), 2)])
