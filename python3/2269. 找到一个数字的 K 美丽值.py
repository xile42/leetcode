class Solution:

    def divisorSubstrings(self, num: int, k: int) -> int:

        s = str(num)
        ns = [s[i-k+1:i+1] for i in range(k-1, len(s)) if int(s[i-k+1:i+1]) != 0 and num % int(s[i-k+1:i+1]) == 0]

        return len(ns)
