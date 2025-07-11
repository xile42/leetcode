class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        ans = 0
        pre = {0}
        acc = list(accumulate(nums))
        offset = 0

        for cur in acc:
            if cur - offset - target in pre:
                ans += 1
                pre = {0}
                offset = cur
            pre.add(cur - offset)

        return ans
