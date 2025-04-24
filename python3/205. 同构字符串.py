class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d = dict()
        dd = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            if t[i] not in dd:
                dd[t[i]] = s[i]
            if d[s[i]] != t[i] or dd[t[i]] != s[i]:
                return False

        return True
        
