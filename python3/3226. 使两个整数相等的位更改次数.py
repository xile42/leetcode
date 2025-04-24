class Solution:

    def minChanges(self, n: int, k: int) -> int:

        cnt = sum(map(int, bin(n ^ k)[2:]))
        bn = bin(n)[2:][::-1]
        bk = bin(k)[2:][::-1]
        if len(bn) < len(bk):
            return -1
        for i in range(len(bk)):
            if bk[i] == "1" and i < len(bn) and bn[i] =="0":
                return -1

        return cnt
        
