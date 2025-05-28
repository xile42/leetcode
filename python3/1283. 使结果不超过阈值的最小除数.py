class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(x):
            return sum(ceil(v / x) for v in nums) <= threshold

        left = 1
        right = 10 ** 9
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
