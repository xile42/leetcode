class Solution:

    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        cnt = [0, 0]
        left = ans = 0
        for right in range(len(s)):
            cnt[int(s[right])] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[int(s[left])] -= 1
                left += 1
            ans += right - left + 1

        return ans
