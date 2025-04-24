class Solution:

    def fillCups(self, amount: List[int]) -> int:

        sa = sorted(amount)
        low, mid, mx = sa

        if low <= mx - mid:
            return mx

        return mx + ceil((low + mid - mx) / 2)
