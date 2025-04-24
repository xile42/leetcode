
class Solution:

    result = list()

    def search(self, nums, current):

        if len(nums) == 0:
            self.result.append(current)

        visited_this_layer = set()
        for idx, num in enumerate(nums):
            if num in visited_this_layer:
                continue
            visited_this_layer.add(num)
            self.search(nums[:idx] + nums[idx + 1:], current + [num])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())

        return self.result
