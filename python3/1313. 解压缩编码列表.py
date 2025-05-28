class Solution:

    def decompressRLElist(self, nums: List[int]) -> List[int]:

        i = 0
        n = len(nums)
        ans = list()
        while 2 * i < n:
            a, b = nums[2 * i], nums[2 * i + 1]
            ans += [b] * a
            i += 1

        return ans
