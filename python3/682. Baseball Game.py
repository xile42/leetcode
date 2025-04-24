class Solution:

    def calPoints(self, operations: List[str]) -> int:

        results = list()
        for op in operations:
            if op == "+":
                results.append(results[-1]+results[-2])
            elif op == "D":
                results.append(results[-1]*2)
            elif op == "C":
                results.pop(-1)
            else:
                results.append(int(op))

        return sum(results)
