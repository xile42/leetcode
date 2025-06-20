class Solution:

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        return sorted([a * x ** 2 + b * x + c for x in nums])
