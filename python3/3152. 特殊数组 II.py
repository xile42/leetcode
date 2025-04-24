class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        ns = [1] + [1 if nums[i] & 1 != nums[i - 1] & 1 else 0 for i in range(1, len(nums))]
        acc = list(accumulate(ns))

        ans = list()
        for l, r in queries:
            ans.append(acc[r] - acc[l] == r - l)

        return ans
