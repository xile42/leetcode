class Solution:

    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:

        base = 1000000007
        a = sorted(staple)
        b = sorted(drinks, reverse=True)
        ans = 0
        i = j = 0
        m = len(a)
        n = len(b)
        while i < m and j < n:
            if a[i] + b[j] <= x:
                ans += (n - j) % base
                i += 1
            else:
                j += 1

        return ans % base
