class Solution:

    def convert(self, s: str, numRows: int) -> str:

        row_lists = [list() for _ in range(numRows)]

        idx = 0
        step = -1 if numRows != 1 else 0
        for char in s:
            row_lists[idx].append(char)
            if idx == 0 or idx == numRows - 1:
                step *= -1
            idx += step

        result = str()
        for row_list in row_lists:
            result += "".join(row_list)

        return result
