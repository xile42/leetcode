class Solution:

    def countElements(self, nums: List[int]) -> int:

        sn = sorted(nums)
        l = 0
        r = len(sn) - 1
        while l < len(sn) and sn[l] == sn[0]:
            l += 1
        while r >= 0 and sn[r] == sn[-1]:
            r -= 1

        return max(r - l + 1, 0)
