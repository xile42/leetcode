class Solution:

    def reverseBits(self, num: int) -> int:

        ans = 1
        l = r = 0
        for _ in range(32):
            n = num & 1

            if n:
                l += 1
            else:
                r = l + 1
                l = 0
            ans = max(ans, l + r)
            num >>= 1

        return ans