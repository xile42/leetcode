class Solution:

    def minLength(self, s: str) -> int:

        l = len(s)
        while True:
            s = s.replace("AB", "").replace("CD", "")
            ll = len(s)
            if l == ll:
                break
            else:
                l = ll

        return len(s)
