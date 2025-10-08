class Solution:

    def splitArray(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        j = n - 1
        while j > 0 and nums[j - 1] > nums[j]:
            j -= 1

        if i + 1 == j and nums[i] == nums[j]:
            return abs(sum(nums[:i + 1]) - sum(nums[j:]))

        if i != j:
            return -1

        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        mid = nums[i]

        return min(abs(left + mid - right), abs(left - (mid + right)))
