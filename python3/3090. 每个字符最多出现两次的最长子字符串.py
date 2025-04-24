class Solution:

    def maximumLengthSubstring(self, s: str) -> int:

        ans = left = 0
        cnt = defaultdict(int)
        for right in range(len(s)):
            cnt[s[right]] += 1
            while any(i > 2 for i in cnt.values()):
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
