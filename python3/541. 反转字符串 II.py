class Solution:

    def reverseStr(self, s: str, k: int) -> str:

        result = str()
        idx = 0
        while idx < len(s):
            t = s[idx:idx+2*k]
            result += t[:k][::-1] + t[k:]
            idx += 2 * k

        return result
        
