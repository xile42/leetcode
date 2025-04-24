class Solution:

    def countGoodSubstrings(self, s: str) -> int:

        if len(s) < 3:
            return 0

        cnt = defaultdict(int)
        for c in s[:3]:
            cnt[c] += 1
        left = ans = 0
        ans += 1 if all(i <= 1 for i in cnt.values()) else 0
        for right in range(3, len(s)):
            cnt[s[right]] += 1
            cnt[s[left]] -= 1
            if all(i <= 1 for i in cnt.values()):
                ans += 1
            left += 1

        return ans
