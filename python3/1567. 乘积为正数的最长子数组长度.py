class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        ans = 0
        left = -1
        cnt = 0
        for right, n in enumerate(nums):
            if n == 0:
                left = right
                cnt = 0
                continue
            elif n > 0:
                if not cnt & 1:
                    ans = max(ans, right - left)
            else:
                cnt += 1
                if not cnt & 1:
                    ans = max(ans, right - left)

        left = -1
        cnt = 0
        for right, n in enumerate(nums[::-1]):
            if n == 0:
                left = right
                cnt = 0
                continue
            elif n > 0:
                if not cnt & 1:
                    ans = max(ans, right - left)
            else:
                cnt += 1
                if not cnt & 1:
                    ans = max(ans, right - left)

        return ans
