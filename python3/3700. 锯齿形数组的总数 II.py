"""
codeforces-python: 算法竞赛Python3模板库
#2: 矩阵快速幂&运算
https://github.com/xile42/codeforces-python/blob/main/templates/math_matrix.py
"""
class Matrix:

    def __init__(self, matrix: List[List[int]], mod: Optional[int] = None) -> None:

        self.matrix = matrix
        self.mod = mod
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0  # 忽略列数相等检查

    @classmethod
    def new_matrix(cls, n: int, m: int, mod: Optional[int] = None) -> "Matrix":

        return Matrix([[0] * m for _ in range(n)], mod)

    def swap_rows(self, i: int, j: int) -> None:

        if not (0 <= i < self.rows and 0 <= j < self.rows):
            raise ValueError("Row index out of range")

        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]

    def swap_cols(self, i: int, j: int) -> None:

        if not (0 <= i < self.cols and 0 <= j < self.cols):
            raise ValueError("Column index out of range")

        for row in self.matrix:
            row[i], row[j] = row[j], row[i]

    def mul_row(self, i: int, k: int) -> None:

        if not 0 <= i < self.rows:
            raise ValueError("Row index out of range")

        for j in range(self.cols):
            self.matrix[i][j] *= k
            if self.mod is not None:
                self.matrix[i][j] %= self.mod

    def trace(self) -> int:

        if self.rows != self.cols:
            raise ValueError("Trace is only defined for square matrices")

        trace = 0
        for i in range(self.rows):
            trace += self.matrix[i][i]
            if self.mod is not None:
                trace %= self.mod

        return trace

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """ self @ other """

        if self.cols != other.rows:
            raise ValueError(f"Matrix dimension mismatch: {self.rows}x{self.cols} * {other.rows}x{other.cols}")

        ans = Matrix.new_matrix(self.rows, other.cols, self.mod)

        for i in range(self.rows):
            for k in range(self.cols):
                if self.matrix[i][k] == 0:
                    continue  # 稀疏矩阵优化
                for j in range(other.cols):
                    ans.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    if self.mod is not None:
                        ans.matrix[i][j] %= self.mod

        return ans

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """ self + other """

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Matrix dimension mismatch: {self.rows}x{self.cols} + {other.rows}x{other.cols}")

        ans = Matrix.new_matrix(self.rows, self.cols, self.mod)

        for i in range(self.rows):
            for j in range(self.cols):
                ans.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                if self.mod is not None:
                    ans.matrix[i][j] %= self.mod

        return ans

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """ self - other """

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Matrix dimension mismatch: {self.rows}x{self.cols} - {other.rows}x{other.cols}")

        ans = Matrix.new_matrix(self.rows, self.cols, self.mod)

        for i in range(self.rows):
            for j in range(self.cols):
                ans.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
                if self.mod is not None:
                    ans.matrix[i][j] = (ans.matrix[i][j] % self.mod + self.mod) % self.mod  # 确保结果为非负数

        return ans

    def pow_mul(self, n: int, f0: Optional["Matrix"] = None) -> "Matrix":
        """ (matrix ^ n) * f0; 若f0 is None: matrix ^ n """

        if f0 is None:

            if self.rows != self.cols:
                raise ValueError("Only square matrices can be raised to a power")
            f0 = Matrix.new_matrix(self.rows, self.rows, self.mod)
            for i in range(self.rows):
                f0.matrix[i][i] = 1  # 初始化为单位矩阵

        elif self.cols != f0.rows:

            raise ValueError(f"Matrix dimension mismatch: {self.rows}x{self.cols} ^ {n} * {f0.rows}x{f0.cols}")

        cur = self
        ans = f0
        while n > 0:
            if n & 1:
                ans = cur @ ans
            cur = cur @ cur
            n >>= 1

        return ans

    def __str__(self) -> str:

        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Matrix):
            return False

        return self.matrix == other.matrix


class Solution:

    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        base = 10 ** 9 + 7
        m = r - l + 1
        size = 2 * m
        T = Matrix.new_matrix(size, size, base)

        for i in range(m):
            for j in range(i):
                T.matrix[i][m + j] = 1
        for i in range(m):
            for j in range(i + 1, m):
                T.matrix[m + i][j] = 1

        f0 = Matrix.new_matrix(size, 1, base)
        for i in range(m):
            f0.matrix[i][0] = i
            f0.matrix[m + i][0] = m - 1 - i

        vector = T.pow_mul(n - 2, f0)
        ans = 0
        for i in range(size):
            ans = (ans + vector.matrix[i][0]) % base

        return ans
