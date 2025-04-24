class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        left = 0
        while left < len(nums) and nums[left] != val:
            left += 1

        if left == len(nums):
            return len(nums)

        for right in range(left + 1, len(nums)):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return left
