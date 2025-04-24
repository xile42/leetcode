class Solution:

    def minWindow(self, s: str, t: str) -> str:

        c = Counter(t)
        left = 0
        ans_l = inf
        ans = ""
        for right in range(len(s)):
            c[s[right]] -= 1
            while all(v <= 0 for v in c.values()):
                if c[s[left]] == 0:
                    cur_l = right - left + 1
                    if cur_l < ans_l:
                        ans = s[left:right + 1]
                        ans_l = cur_l
                    break
                else:
                    c[s[left]] += 1
                    left += 1

        return ans
