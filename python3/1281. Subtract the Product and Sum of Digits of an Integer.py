class Solution:

    def subtractProductAndSum(self, n: int) -> int:

        nums = [int(i) for i in str(n)]
        return reduce(mul, nums) - reduce(add, nums)
