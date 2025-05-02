class Solution:

    def smallestNumber(self, n: int) -> int:

        ans = 0
        for i in range(n.bit_length()):
            ans |= (1 << i)

        return ans