class Solution:

    def largestInteger(self, num: int) -> int:

        ns = list(map(int, str(num)))
        odds = sorted([i for i in ns if i & 1], reverse=True)
        even = sorted([i for i in ns if not i & 1], reverse=True)
        ans = str()
        for c in str(num):
            if int(c) & 1:
                ans += str(odds.pop(0))
            else:
                ans += str(even.pop(0))

        return int(ans)
