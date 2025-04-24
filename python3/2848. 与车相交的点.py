class Solution:

    def numberOfPoints(self, nums: List[List[int]]) -> int:

        diff = [0] * 102
        for l, r in nums:
            diff[l] += 1
            diff[r + 1] -= 1

        acc = list(accumulate(diff))
        return sum([acc[i] > 0 for i in range(1, 100 + 1)])
