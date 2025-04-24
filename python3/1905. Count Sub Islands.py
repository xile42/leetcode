# You are given two m x n binary matrices grid1 and grid2 containing only 0's (
# representing water) and 1's (representing land). An island is a group of 1's
# connected 4-directionally (horizontal or vertical). Any cells outside of the grid
# are considered water cells.
#
#  An island in grid2 is considered a sub-island if there is an island in grid1
# that contains all the cells that make up this island in grid2.
#
#  Return the number of islands in grid2 that are considered sub-islands.
#
#
#  Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
#
#
#  Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
#
#
#
#  Constraints:
#
#
#  m == grid1.length == grid2.length
#  n == grid1[i].length == grid2[i].length
#  1 <= m, n <= 500
#  grid1[i][j] and grid2[i][j] are either 0 or 1.
#
#
#  Related Topics Array Depth-First Search Breadth-First Search Union Find
# Matrix 👍 2271 👎 71


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def check(self, idx, jdx, m, n):

        results = list()
        offsets = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        for offset_i, offset_j in offsets:
            iidx = idx + offset_i
            jjdx = jdx + offset_j
            if 0 <= iidx < m and 0 <= jjdx < n:
                results.append([iidx, jjdx])

        return results

    def search(self, grid1, grid2):

        m, n = len(grid1), len(grid1[0])

        for idx in range(m):
            for jdx in range(n):

                if self.visit[idx][jdx] or grid2[idx][jdx] == 0:
                    continue

                queue = list()
                queue.append([idx, jdx])
                success_flag = True
                while len(queue) != 0:
                    iidx, jjdx = queue.pop(0)
                    self.visit[iidx][jjdx] = True
                    if success_flag and grid1[iidx][jjdx] == 0:
                        success_flag = False
                    for neighbour_idx, neighbour_jdx in self.check(iidx, jjdx, m, n):
                        if self.visit[neighbour_idx][neighbour_jdx] or grid2[neighbour_idx][neighbour_jdx] == 0:
                            continue
                        self.visit[neighbour_idx][neighbour_jdx] = True
                        if success_flag and grid1[neighbour_idx][neighbour_jdx] == 0:
                            success_flag = False
                        queue.append([neighbour_idx, neighbour_jdx])
                if success_flag:
                    self.result += 1

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m, n = len(grid1), len(grid1[0])

        self.result = 0
        self.visit = [[False for _ in range(n)] for _ in range(m)]
        self.search(grid1, grid2)

        return self.result

# leetcode submit region end(Prohibit modification and deletion)
