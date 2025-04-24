class Solution:

    def mySqrt(self, x: int) -> int:

        l = 0
        r = x
        while l <= r:
            m = l + (r - l) // 2
            if m ** 2 >= x:
                r = m - 1
            else:
                l = m + 1

        return max(l if l ** 2 == x else l - 1, 0)
