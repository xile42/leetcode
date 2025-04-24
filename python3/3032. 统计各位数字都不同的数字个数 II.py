class Solution:

    def numberCount(self, a: int, b: int) -> int:

        ans = 0
        for i in range(a, b + 1):
            ans += len(Counter(str(i))) == len(str(i))

        return ans
