class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        left = 1
        right = position[-1]

        def check(x):

            cnt = 1
            cur = position[0]
            for i in position[1:]:
                if i - cur >= x:
                    cnt += 1
                    cur = i
                if cnt >= m:
                    return True

            return False

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
            
