class Solution:

    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        d = {n: i for i, n in enumerate(nums)}
        for a, b in operations:
            i = d[a]
            del d[a]
            d[b] = i
            nums[i] = b

        return nums
