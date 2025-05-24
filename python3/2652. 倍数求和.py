class Solution:

    def sumOfMultiples(self, n: int) -> int:

        t = [False] * (n + 1)
        ans = 0
        for d in [3, 5, 7]:
            cur = 0
            while (cur := cur + d) <= n:
                if t[cur]:
                    continue
                t[cur] = True
                ans += cur

        return ans