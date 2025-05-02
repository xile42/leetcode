class Solution:

    def hasMatch(self, s: str, p: str) -> bool:

        if p == "*":
            return True

        def check(s, start, tar):

            l = len(tar)
            if l == 0:
                return start
            for i in range(start, len(s)):
                if s[i:i+l] == tar:
                    return i + l
            return None

        pre, suf = p.split("*")
        res = check(s, 0, pre)
        if res is None:
            return False
        res = check(s, res, suf)
        if res is None:
            return False

        return True
