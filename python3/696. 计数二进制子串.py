class Solution:

    def countBinarySubstrings(self, s: str) -> int:

        cnt = list()
        idx = 0
        while idx < len(s):
            c = s[idx]
            idx += 1
            t = 1
            while idx < len(s) and s[idx] == c:
                t += 1
                idx += 1
            cnt.append(t)

        result = 0
        for idx in range(len(cnt)-1):
            result += min(cnt[idx], cnt[idx+1])

        return result
        
