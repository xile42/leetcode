class Solution:

    def maximumTotalSum(self, maximumHeight: List[int]) -> int:

        maximumHeight.sort()
        for idx, height in enumerate(maximumHeight):
            if idx + 1 > height:
                return -1

        result = 0
        current = maximumHeight[-1]
        for height in maximumHeight[::-1]:
            if current <= height:
                result += current
                current -= 1
            else:
                current = height - 1
                result += height

        return result
