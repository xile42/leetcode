class Solution:

    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        sn = sorted(nums)
        ans = [i for i in range(len(sn)) if sn[i] == target]

        return ans
