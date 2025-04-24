class Solution:

    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        result = 0
        if income <= brackets[0][0]:
            return income * brackets[0][1] / 100
        else:
            result += brackets[0][0] * brackets[0][1] / 100
        for idx, (v, p) in enumerate(brackets):
            if idx == 0:
                continue
            if income <= v:
                result += (income - brackets[idx-1][0]) * p / 100
                return result
            else:
                result += (v - brackets[idx-1][0]) * p / 100

        return result
