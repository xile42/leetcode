class Solution:

    def leftRightDifference(self, nums: List[int]) -> List[int]:

        acc = [0] + list(accumulate(nums))
        ans = list()
        for i in range(len(nums)):
            l = acc[i]
            r = 0 if i == len(nums) - 1 else acc[-1] - acc[i + 1]
            ans.append(abs(l - r))

        return ans
