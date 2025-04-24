class Solution:

    def arraySign(self, nums: List[int]) -> int:

        res = reduce(mul, nums)
        
        return 0 if res == 0 else (1 if res > 0 else -1)
