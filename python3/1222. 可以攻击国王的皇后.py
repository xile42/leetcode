class Solution:

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        s = set(map(tuple, queens))
        ans = []
        for dx, dy in (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1):
            x, y = king[0] + dx, king[1] + dy  # 国王朝 (dx,dy) 方向发射一条射线
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in s:  # 射线首次遇到皇后
                    ans.append([x, y])
                    break
                x += dx
                y += dy  # 射线没有遇到皇后，继续往前走

        return ans
