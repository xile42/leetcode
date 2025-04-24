MX = 31622
pi = [0] * (MX + 1)
for i in range(2, MX + 1):
    if pi[i] == 0:  # i 是质数
        pi[i] = pi[i - 1] + 1
        for j in range(i * i, MX + 1, i):
            pi[j] = -1  # 标记 i 的倍数为合数
    else:
        pi[i] = pi[i - 1]

class Solution:

    def nonSpecialCount(self, l: int, r: int) -> int:

        return r - l + 1 - (pi[isqrt(r)] - pi[isqrt(l - 1)])
