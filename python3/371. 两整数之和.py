class Solution:

    def getSum(self, a: int, b: int) -> int:

        x = (2 ** a) * (2 ** b)

        return int(math.log(x,2))
