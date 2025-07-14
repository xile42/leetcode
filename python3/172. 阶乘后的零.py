from typing import *
from operator import *
from functools import reduce


"""
codeforces-python: 算法竞赛Python3模板库
#2: 欧拉筛
https://github.com/xile42/codeforces-python/blob/main/templates/math.py
"""
class EulerSieve:

    def __init__(self, mx: int=10 ** 5 + 2, need_factors: bool=False, need_lpf: bool=False) -> None:

        self.is_prime = [True] * mx
        self.is_prime[0] = self.is_prime[1] = False  # 忽略了越界检查
        self.primes = list()  # 所有质数

        if need_factors:
            self.factors = [[] for _ in range(mx)]  # 有重复质因数列表

        if need_lpf:
            # lpf[x] = 0  x <= 1, 无意义
            # lpf[x] = x  x 是质数
            # lpf[x] = y  x 是合数, 则 y 是 x 的最小质因数
            self.lpf = [0] * mx

        for i in range(2, mx):

            if self.is_prime[i]:
                self.primes.append(i)
                if need_factors:
                    self.factors[i].append(i)
                if need_lpf:
                    self.lpf[i] = i

            for p in self.primes:

                if i * p >= mx:
                    break

                self.is_prime[i * p] = False

                if need_factors:
                    self.factors[i * p] = self.factors[i].copy()  # 复制i的质因数
                    self.factors[i * p].append(p)  # 添加当前质数p

                if need_lpf:
                    if self.lpf[i * p] == 0:
                        self.lpf[i * p] = p  # 最小质因子

                if i % p == 0:  # 保证每个合数只被最小质因数筛一次
                    break

    def factorize(self, x: int) -> Dict[int, int]:

        assert hasattr(self, 'lpf'), "LPF array not initialized. Set need_lpf=True in constructor."

        if x < 2:
            return dict()

        factors = dict()
        while x > 1:
            lpf = self.lpf[x]
            factors[lpf] = factors.get(lpf, 0) + 1
            x //= lpf

        return factors


class Solution:

    def trailingZeroes(self, n: int) -> int:

        # solution #1
        es = EulerSieve(mx=10 ** 4 + 1, need_factors=True)
        c2 = c5 = 0
        for i in range(1, n + 1):
            counter = Counter(es.factors[i])
            c2 += counter[2]
            c5 += counter[5]

        return min(c2, c5)

        # # solution #2
        # es = EulerSieve(need_lpf=True)
        # c2 = c5 = 0
        # for i in range(1, n + 1):
        #     factors = es.factorize(i)
        #     if 2 in factors:
        #         c2 += factors[2]
        #     if 5 in factors:
        #         c5 += factors[5]
        #
        # return min(c2, c5)
