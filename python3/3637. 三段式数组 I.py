class Solution:

    def isTrionic(self, nums: List[int]) -> bool:

        n = len(nums)

        i = 1
        while i < n - 1 and nums[i] > nums[i - 1]:
            i += 1

        j = n - 2
        while j > 0 and nums[j] < nums[j + 1]:
            j -= 1

        i -= 1
        j += 1

        if i == n - 1 or j == 0 or i >= j or i == 0 or j == n - 1:
            return False

        for k in range(i + 1, j + 1):
            if nums[k] >= nums[k - 1]:
                return False

        return True
