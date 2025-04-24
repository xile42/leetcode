class Solution:

    def minDeletions(self, s: str) -> int:

        cnt = Counter(s)
        ns = sorted(cnt.values(), reverse=True)
        cur = ns[0]
        ans = 0
        for n in ns:
            ans += max(n - cur, 0)
            cur = max(min(n - 1, cur - 1), 0)

        return ans
