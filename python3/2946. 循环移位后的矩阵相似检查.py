class Solution:

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        ans = list()
        n = len(mat[0])
        t = k % n
        if t == 0:
            return True
        for i, row in enumerate(mat):
            if i & 1:
                ans.append(row[-t:] + row[:n - t])
            else:
                ans.append(row[t:] + row[:t])

        return ans == mat
