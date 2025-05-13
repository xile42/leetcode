class Solution:

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        x = gcd(*numsDivide)
        ans = 0
        nums.sort()
        for v in nums:
            if v == x or x % v == 0:
                return ans
            ans += 1

        return -1
