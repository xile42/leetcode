class Solution:

    def minOperations(self, s: str) -> int:

        ans = 0
        cnt = Counter()
        for c in s:
            if c == "a":
                continue
            d = ord(c) - ord("a")
            cnt[d] += 1

        for i in range(1, 26):
            if cnt[i] > 0:
                ans += 1
                cnt[i + 1] += cnt[i]

        return ans
