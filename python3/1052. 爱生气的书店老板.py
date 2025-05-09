class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        base = sum(n for i, n in enumerate(customers) if grumpy[i] == 0)
        ns = [0 if grumpy[i] == 0 else customers[i] for  i in range(len(customers))]
        s = 0
        k = minutes
        ans = 0
        for i, v in enumerate(ns):
            s += v
            if i >= k:
                s -= ns[i - k]
            if i >= k - 1:
                ans = max(ans, s)

        return base + ans
