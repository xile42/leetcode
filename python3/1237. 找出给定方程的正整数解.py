"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:

    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ans = list()
        for x in range(1, 1000 + 1):
            mn = customfunction.f(x, 0)
            mx = customfunction.f(x, 1000)
            if mn > z:
                break
            if not (mn < z < mx):
                continue
            left = 1
            right = 1000
            while left <= right:
                mid = (left + right) // 2
                if (value := customfunction.f(x, mid)) == z:
                    left = mid
                    break
                elif value > z:
                    right = mid - 1
                else:
                    left = mid + 1
            if customfunction.f(x, left) == z:
                ans.append([x, left])

        return ans
