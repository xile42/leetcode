class Solution:

    def minOperations(self, nums: List[int]) -> int:

        ans = 0
        mx_length = 0
        for n in nums:
            length = n.bit_length()
            mx_length = max(mx_length, length - 1)
            ans += n.bit_count()

        return ans + mx_length
