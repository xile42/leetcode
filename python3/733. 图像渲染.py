class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(i, j, tar_c):

            nonlocal image, vis

            vis[i][j] = True
            image[i][j] = color

            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < len(image) and 0 <= jj < len(image[0]):
                    if not vis[ii][jj] and image[ii][jj] == tar_c:
                        f(ii, jj, tar_c)

        f(sr, sc, image[sr][sc])

        return image
