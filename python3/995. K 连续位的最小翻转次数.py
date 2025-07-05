class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:

        ans = 0
        n = len(nums)
        diff = [0] * (n + 1)

        cur = 0
        for i, v in enumerate(nums):
            cur += diff[i]
            c = 1 - v if cur & 1 else v
            if c == 0:
                ans += 1
                cur += 1
                if i + k <= n:
                    diff[i + k] -= 1
                else:
                    return -1

        return ans
