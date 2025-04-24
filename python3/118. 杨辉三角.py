class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]
        while len(ans) < numRows:
            ans.append( [1] + [ans[-1][i] + ans[-1][i - 1] for i in range(1, len(ans[-1]))] + [1] )

        return ans
