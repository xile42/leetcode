class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:

        ns = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] != ns[i]:
                left = i
                break
        else:
            return 0
        for i in range(n - 1, -1, -1):
            if nums[i] != ns[i]:
                right = i
                break

        return right - left + 1
