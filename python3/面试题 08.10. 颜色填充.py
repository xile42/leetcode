class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        ans = image.copy()
        vis = set()
        tar = image[sr][sc]
        
        def f(i, j):

            nonlocal ans
            ans[i][j] = newColor
            vis.add((i, j))

            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in vis and image[ii][jj] == tar:
                    f(ii, jj)

        f(sr, sc)

        return ans
