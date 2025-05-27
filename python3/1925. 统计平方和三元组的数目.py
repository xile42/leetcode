d = dict()
rd = dict()
s = set()
for i in range(1, 250 + 1):
    t = i * i
    s.add(t)
    d[i] = t
    rd[t] = i

class Solution:

    def countTriples(self, n: int) -> int:

        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if d[i] + d[j] in s and rd[d[i] + d[j]] <= n:
                    ans += 2

        return ans