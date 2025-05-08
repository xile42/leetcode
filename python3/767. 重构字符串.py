class Solution:

    def reorganizeString(self, s: str) -> str:

        cnt = Counter(s)
        mx = max(cnt.values())
        for k in cnt:
            if cnt[k] == mx:
                c = k
                break
        if cnt[c] > ceil(len(s) / 2):
            return ""

        ans = [""] * len(s)
        ans[:cnt[c] * 2:2] = [c] * cnt[c]
        cur = cnt[c] * 2
        del cnt[c]

        for k, v in cnt.items():
            for _ in range(v):
                if cur >= len(s):
                    cur = 1
                ans[cur] = k
                cur += 2

        return "".join(ans)
