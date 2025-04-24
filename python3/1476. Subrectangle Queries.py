class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):

        self.nums = rectangle
        self.m, self.n = len(rectangle), len(rectangle[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                if 0 <= i < self.m and 0 <= j < self.n:
                    self.nums[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:

        return self.nums[row][col]
