class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        pos = sorted([n for n in nums if n >= 0])
        neg = sorted([n for n in nums if n < 0])
        flag = 0 in nums
        cnt = len(neg)

        if k <= cnt:
            return -sum(neg[:k]) + sum(neg[k:]) + sum(pos)

        rem = k - cnt
        if flag or not rem & 1:
            return -sum(neg) + sum(pos)
        
        min_abs = min(abs(n) for n in nums)
        return -sum(neg) + sum(pos) - 2 * min_abs
