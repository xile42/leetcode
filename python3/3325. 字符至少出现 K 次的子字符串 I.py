class Solution:

    def numberOfSubstrings(self, s: str, k: int) -> int:

        cnt = Counter()
        ans = left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[s[left]] -= 1
                left += 1
            ans += left

        return ans
