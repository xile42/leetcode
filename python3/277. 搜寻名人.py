# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:

    def findCelebrity(self, n: int) -> int:

        for i in range(n):
            if all(knows(j, i) and not knows(i, j) for j in range(n) if i != j):
                return i

        return -1
