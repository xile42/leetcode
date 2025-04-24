class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m, n = len(img), len(img[0])

        def f(x, y):

            vs = list()
            for xx, yy in (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1):
                if 0 <= xx < m and 0 <= yy < n:
                    vs.append(img[xx][yy])

            return int(mean(vs))

        results = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                results[x][y] = f(x, y)

        return results
