class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        ans = cur = 0
        d = {c: i for i, c in enumerate("croak")}
        cnt = Counter()

        for c in croakOfFrogs:
            i = d[c]
            cnt[c] += 1
            if c == "c":
                cur += 1
                ans = max(ans, cur)
            for cc in "croak":
                j = d[cc]
                if j < i and cnt[cc] < cnt[c]:
                    return -1
            if c == "k":
                cur -= 1
                for cc in "croak":
                    cnt[cc] -= 1

        return ans if all(cnt[c] == 0 for c in "croak") else -1
