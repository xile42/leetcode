class Solution:

    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:

        ans = 0
        cur_x = startPos[0]
        offset = 1 if homePos[0] >= startPos[0] else -1
        while cur_x != homePos[0]:
            cur_x += offset
            ans += rowCosts[cur_x]
        cur_y = startPos[1]
        offset = 1 if homePos[1] >= startPos[1] else -1
        while cur_y != homePos[1]:
            cur_y += offset
            ans += colCosts[cur_y]

        return ans
