class Solution:

    def isPerfectSquare(self, num: int) -> bool:

        def check(i):
            t = i * i
            if t == num:
                return 1
            elif t < num:
                return 0
            else:
                return 2

        left = 1
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            t = check(mid)
            if t == 1:
                return True
            if t == 0:
                left = mid + 1
            else:
                right = mid - 1

        return True if left * left == num else False
