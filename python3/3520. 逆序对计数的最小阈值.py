class Solution:

    def minThreshold(self, nums: List[int], k: int) -> int:

        def check(x):

            ns = SortedList()
            ans = 0
            for n in nums:
                ans += bisect_right(ns, n + x) - bisect_left(ns, n + 1)
                ns.add(n)
                if ans >= k:
                    return True

            return False

        left, right = 0, max(nums)
        if not check(max(nums)):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
