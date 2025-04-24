class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        n = len(s)
        ans = left = 0
        cnt = Counter()
        for right, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans
