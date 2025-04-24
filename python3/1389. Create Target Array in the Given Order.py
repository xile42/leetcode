class Solution:

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        result = list()
        for _, (num, idx) in enumerate(zip(nums, index)):
            result.insert(idx, num)

        return result
