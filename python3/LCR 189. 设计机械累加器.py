class Solution:

    def __init__(self):

        self.res = 0

    def mechanicalAccumulator(self, target: int) -> int:

        target > 1 and self.mechanicalAccumulator(target - 1)
        self.res += target

        return self.res