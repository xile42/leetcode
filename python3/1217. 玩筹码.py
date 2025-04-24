class Solution:

    def minCostToMoveChips(self, position: List[int]) -> int:

        a, b = sum(1 for v in position if v & 1), sum(1 for v in position if not v & 1)

        return min(a, b)        
