class Solution:

    def minOperations(self, s: str) -> int:

        n = len(s)
        base = ["0"] * n
        t1 = [base[i] if i & 1 else "1" for i in range(n)]
        t2 = [base[i] if not i & 1 else "1" for i in range(n)]
        r1 = sum([1 if t1[i] != s[i] else 0 for i in range(n)])
        r2 = sum([1 if t2[i] != s[i] else 0 for i in range(n)])

        return min(r1, r2)
