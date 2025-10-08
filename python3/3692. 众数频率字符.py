class Solution:

    def majorityFrequencyGroup(self, s: str) -> str:

        cnt = Counter(s)
        mx = max(cnt.values())

        ans = list()
        cur = -inf
        for k in range(mx, 0, -1):
            cs = [c for c in cnt if cnt[c] == k]
            l = len(cs)
            if l > cur:
                ans = cs
                cur = l

        return "".join(ans)
