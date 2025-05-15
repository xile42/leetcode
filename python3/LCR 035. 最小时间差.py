class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:

        nums = sorted([int(i[:2]) * 60 + int(i[-2:]) for i in timePoints])
        nums += [i + 24 * 60 for i in nums]
        result = min([nums[idx]-nums[idx-1] for idx in range(1, len(nums))])

        return result