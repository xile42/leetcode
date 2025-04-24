class Solution:

    def getRow(self, rowIndex: int) -> List[int]:

        ans = [[1]]
        while len(ans) < rowIndex + 1:
            ans.append( [1] + [ans[-1][i] + ans[-1][i - 1] for i in range(1, len(ans[-1]))] + [1] )

        return ans[-1]
