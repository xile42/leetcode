class Solution:

    def maximumTastiness(self, price: List[int], k: int) -> int:

        price.sort()

        def check(x):

            cnt = 0
            pre = -inf
            for n in price:
                if n - pre >= x:
                    cnt += 1
                    pre = n

            return cnt >= k

        left = 0
        right = price[-1] - price[0]
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
