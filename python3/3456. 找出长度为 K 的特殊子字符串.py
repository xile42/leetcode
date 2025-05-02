class Solution:

    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n):
            ss = s[i:i + k]
            if len(ss) < k:
                break
            c = Counter(ss)
            if len(c) > 1:
                continue
            key = list(c.keys())[0]
            if (i - 1 >= 0 and s[i - 1] == key) or (i + k < n and s[i + k] == key):
                continue
            return True

        return False
