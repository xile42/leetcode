class Solution:

    operations = {"+", "-", "*"}

    def search(self, start, end):

        s = self.s[start:end]

        split_idx_list = list()
        for idx, char in enumerate(s):
            if char in self.operations:
                split_idx_list.append(idx)

        if len(split_idx_list) == 0:
            return [int(self.s[start:end])]

        results = list()
        for root_idx in split_idx_list:
            operation = s[root_idx]
            left_values = self.search(start, start+root_idx)
            right_values = self.search(start+root_idx+1, end)
            for left_value in left_values:
                for right_value in right_values:
                    result = left_value+right_value if operation == "+" else (left_value-right_value if operation == "-" else left_value*right_value)
                    results.append(result)

        return results

    def diffWaysToCompute(self, expression: str) -> List[int]:

        self.s = expression
        results = self.search(0, len(expression))

        return results
