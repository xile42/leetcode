class Solution:

    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        odds = sorted(nums[1::2], reverse=True)
        even = sorted(nums[::2])

        ans = reduce(add, [[i, j] for i, j in zip(even, odds)], [])
        if len(odds) > len(even):
            ans.append(odds[-1])
        elif len(odds) < len(even):
            ans.append(even[-1])

        return ans
