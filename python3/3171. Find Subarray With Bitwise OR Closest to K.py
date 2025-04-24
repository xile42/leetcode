class Solution:

    def minimumDifference(self, nums: List[int], k: int) -> int:

        result = float("inf")
        for idx in range(len(nums)):
            result = min(result, abs(k-nums[idx]))
            jdx = idx - 1
            while jdx >= 0 and (nums[jdx] | nums[idx]) != nums[jdx]:
                nums[jdx] |= nums[idx]
                result = min(result, abs(k-nums[jdx]))
                jdx -= 1

        return result
