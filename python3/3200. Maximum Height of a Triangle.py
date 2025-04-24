class Solution:

    def calculate(self, balls):

        idx = 0
        height = 0
        current = 1
        while True:
            if current > balls[idx]:
                return height
            balls[idx] -= current
            height += 1
            idx = 1 - idx
            current += 1

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        return max(self.calculate([red, blue]), self.calculate([blue, red]))
