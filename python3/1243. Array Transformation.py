class Solution:

    def transform(self, nums):

        result = [nums[0]]
        for idx, value in enumerate(nums):
            if idx == 0 or idx == len(nums) - 1:
                continue
            if value < nums[idx-1] and value < nums[idx+1]:
                result.append(value+1)
            elif value > nums[idx-1] and value > nums[idx+1]:
                result.append(value-1)
            else:
                result.append(value)

        if len(nums) > 1:
            result.append(nums[-1])

        return result

    def transformArray(self, arr: List[int]) -> List[int]:

        while True:
            nums = self.transform(arr)
            if nums == arr:
                return nums
            else:
                arr = nums
