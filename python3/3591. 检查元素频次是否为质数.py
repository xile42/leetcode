"""
codeforces-python: 算法竞赛Python3模板库
#1: 埃氏筛
https://github.com/xile42/codeforces-python/blob/main/templates/math.py
"""
class EratosthenesSieve:

    def __init__(self, mx: int=10 ** 5 + 2, need_factors: bool=False, need_lpf: bool=False) -> None:

        self.is_prime = [True] * mx
        self.is_prime[0] = self.is_prime[1] = False  # 忽略了越界检查

        if need_factors:
            self.factors = [[] for _ in range(mx)]  # 无重复质因数列表

        if need_lpf:
            # lpf[x] = 0  x <= 1, 无意义
            # lpf[x] = x  x 是质数
            # lpf[x] = y  x 是合数, 则 y 是 x 的最小质因数
            self.lpf = [0] * mx

        for i in range(2, mx):

            if not self.is_prime[i]:
                continue

            if need_factors:
                self.factors[i].append(i)

            if need_lpf:
                self.lpf[i] = i  # 质数的最小质因子是自身

            for j in range((i + i) if need_factors else (i * i), mx, i):  # 仅筛质数可以从i * i开始, 求质因数只能从i + i开始; 前者更快但不影响时间复杂度
                self.is_prime[j] = False
                if need_factors:
                    self.factors[j].append(i)
                if need_lpf and self.lpf[j] == 0:
                    self.lpf[j] = i  # 记录最小质因子

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

    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        es = EratosthenesSieve(mx=100 + 1)

        return any(es.is_prime[f] for f in Counter(nums).values())
