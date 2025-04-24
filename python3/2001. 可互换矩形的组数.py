class Solution:

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        ans = 0
        cnt = Counter()
        for w, h in rectangles:
            r = w / h
            ans += cnt[r]
            cnt[r] += 1

        return ans
