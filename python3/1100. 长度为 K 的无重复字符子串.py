class Solution:

    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        ans = 0
        cnt = Counter()
        for i, c in enumerate(s):
            cnt[c] += 1
            if i >= k:
                cc = s[i - k]
                cnt[cc] -= 1
                if cnt[cc] == 0:
                    del cnt[cc]
            if i >= k - 1 and len(cnt) == k:
                ans += 1

        return ans
