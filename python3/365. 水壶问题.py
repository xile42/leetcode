class Solution:

    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        k = gcd(x, y)

        return target <= x + y and target % k == 0
