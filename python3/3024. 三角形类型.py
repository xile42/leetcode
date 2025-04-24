class Solution:

    def triangleType(self, nums: List[int]) -> str:

        a, b, c = nums
        if not (a + b > c and b + c > a and c + a > b):
            return "none"

        l = len(set(nums))
        return "equilateral" if l == 1 else ("isosceles" if l == 2 else "scalene")
