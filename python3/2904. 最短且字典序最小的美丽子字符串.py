class Solution:

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        left = 0
        cnt = 0
        curl = inf
        ans = str()

        for right, c in enumerate(s):
            cnt += int(c)
            while cnt > k or (cnt == k and s[left] == "0"):
                cnt -= int(s[left])
                left += 1
            if cnt == k and (right - left + 1 < curl or (right - left + 1 == curl and s[left:right + 1] < ans)):
                curl = right - left + 1
                ans = s[left:right + 1]

        return ans
