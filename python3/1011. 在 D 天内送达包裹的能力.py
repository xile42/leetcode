class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(w):

            cnt = 1
            cur = 0
            for v in weights:
                if cur + v > w:
                    cnt += 1
                    cur = 0
                cur += v
            
            return cnt <= days

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
