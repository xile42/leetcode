class Solution:

    def minimumRightShifts(self, nums: List[int]) -> int:

        cnt = 0
        idxs = list()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cnt += 1
                idxs.append(i)

        return -1 if cnt > 1 else (0 if cnt == 0 else (-1 if nums[-1] >= nums[0] else len(nums) - idxs[0]))
