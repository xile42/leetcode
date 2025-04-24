class Solution:

    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        grid = list(zip(*grid))
        ans = [max([len(str(i)) for i in row]) for row in grid]

        return ans
