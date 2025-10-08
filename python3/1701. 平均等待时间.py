class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        finish = dict()
        cur = 0
        for i, (start, need) in enumerate(customers):
            end = max(cur, start) + need
            finish[i] = end
            cur = end

        ans = 0
        for i, (start, need) in enumerate(customers):
            ans += finish[i] - start

        return ans / len(customers)
