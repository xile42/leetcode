class Solution:

    def longestPrefix(self, s: str) -> str:

        m = len(s)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = s[i]
            while c and s[c] != v:
                c = pi[c - 1]
            if s[c] == v:
                c += 1
            pi[i] = c
        print(pi)
        return s[:pi[-1]]
