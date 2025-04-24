class Solution:

    def hIndex(self, citations: List[int]) -> int:

        def check(v):

            return sum(1 if n >= v else 0 for n in citations) >= v

        left = 0
        right = max(citations)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
