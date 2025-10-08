class Solution:

    def evenNumberBitwiseORs(self, nums: List[int]) -> int:

        ns = [i for i in nums if not i & 1]

        ans = 0
        for i in ns:
            ans |= i

        return ans
