class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])
        ans = list()
        for tar in range(m + n - 1):
            this_ans = list()
            for i in range(min(m, tar + 1)):
                j = tar - i
                if 0 <= j < n:
                    this_ans.append(mat[i][j])
            if not tar & 1:
                this_ans = this_ans[::-1]
            ans += this_ans

        return ans
