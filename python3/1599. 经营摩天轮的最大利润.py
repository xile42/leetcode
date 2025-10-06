class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        ans = 0
        cur_max = -inf
        left = 0
        cur = 0
        for i, v in enumerate(customers):
            cur -= runningCost
            left += v
            t = min(4, left)
            left -= t
            cur += t * boardingCost
            if cur > cur_max:
                cur_max = cur
                ans = i + 1
        i = len(customers)
        while left:
            cur -= runningCost
            t = min(4, left)
            left -= t
            cur += t * boardingCost
            if cur > cur_max:
                cur_max = cur
                ans = i + 1
            i += 1

        return ans if cur_max > 0 else -1
