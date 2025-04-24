class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        s = set()
        ans = [None, None]
        for n in reduce(add, grid):
            if n in s:
                ans[0] = n
                break
            s.add(n)

        ans[1] = (len(grid) * len(grid) * (len(grid) * len(grid) + 1)) // 2 - (sum(reduce(add, grid)) - ans[0])

        return ans
