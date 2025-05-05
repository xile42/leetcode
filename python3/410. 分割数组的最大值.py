class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:

        def check(x):

            ans = 1
            cur = 0
            for n in nums:
                if n > x:
                    return False
                if cur + n > x:
                    cur = 0
                    ans += 1
                cur += n

            return ans <= k

        left = 0
        right = sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
