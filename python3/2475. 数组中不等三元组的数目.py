class Solution:

    def unequalTriplets(self, nums: List[int]) -> int:

        c = Counter(nums)
        sk = sorted(c.keys())
        ans = 0
        for i in range(len(sk)):
            ki = sk[i]
            for j in range(i + 1, len(sk)):
                kj = sk[j]
                for k in range(j + 1, len(sk)):
                    kk = sk[k]
                    ans += c[ki] * c[kj] * c[kk]

        return ans
