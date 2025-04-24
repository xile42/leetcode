class Solution:

    def minElement(self, nums: List[int]) -> int:

        values = [sum(list(map(int, str(i)))) for i in nums]
        return min(values)
