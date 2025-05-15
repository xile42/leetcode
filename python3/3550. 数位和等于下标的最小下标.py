class Solution:

    def smallestIndex(self, nums: List[int]) -> int:

        ans = -1
        for i, n in enumerate(nums):
            if sum(map(int, map(str, str(n)))) == i:
                ans = i
                break

        return ans
