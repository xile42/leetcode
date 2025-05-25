class Solution:

    def matrixSum(self, nums: List[List[int]]) -> int:

        ns = [sorted(row) for row in nums]
        ans = 0
        for row in zip(*ns):
            ans += max(row)

        return ans
