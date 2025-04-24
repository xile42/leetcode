class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:

        p = list(pattern)
        s = s.strip().split(" ")
        d = dict()
        dd = dict()
        
        if len(p) != len(s):
            return False
        
        for pp, ss in zip(p, s):
            if pp not in d:
                d[pp] = ss
            elif d[pp] != ss:
                return False
            if ss not in dd:
                dd[ss] = pp
            elif dd[ss] != pp:
                return False

        return True
        
