class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        results = list()
        order = 0  # 0-r 1-d 2-l 3-u
        offset_map = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0],
        }
        m, n = len(matrix), len(matrix[0])
        mn = m * n
        visit = [[False for _ in range(n)] for _ in range(m)]

        idx, jdx = 0, 0
        visit[0][0] = True
        results.append(matrix[0][0])

        while len(results) != mn:

            offset_idx, offset_jdx = offset_map[order]

            while 0 <= idx + offset_idx < m and 0 <= jdx + offset_jdx < n and not visit[idx+offset_idx][jdx+offset_jdx]:
                results.append(matrix[idx+offset_idx][jdx+offset_jdx])
                visit[idx+offset_idx][jdx+offset_jdx] = True
                idx += offset_idx
                jdx += offset_jdx

            order = 0 if order == 3 else order + 1

        return results
