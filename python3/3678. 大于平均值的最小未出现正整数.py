class Solution:

    def smallestAbsent(self, nums: List[int]) -> int:

        mean = sum(nums) / len(nums)
        s = set(nums)
        for i in count(max(ceil(mean), 1)):
            if i > mean and i not in s:
                return i
