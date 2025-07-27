class Solution:

    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        i = start = 0
        while start < len(nums):
            if groups[i] == nums[start:start + len(groups[i])]:
                start += len(groups[i])
                i += 1
                if i >= len(groups):
                    return True
            else:
                start += 1

        return False
