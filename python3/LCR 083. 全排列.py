class Solution:

    result = list()

    def search(self, nums, current):

        if len(nums) == 0:
            self.result.append(current)

        for idx, num in enumerate(nums):
            self.search(nums[:idx]+nums[idx+1:], current+[num])

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())

        return self.result
