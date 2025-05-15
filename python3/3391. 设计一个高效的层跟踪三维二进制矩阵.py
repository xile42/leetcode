class Matrix3D:

    def __init__(self, n: int):

        self.ns = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        self.cnt = [0] * n

    def setCell(self, x: int, y: int, z: int) -> None:

        if not self.ns[x][y][z]:
            self.cnt[x] += 1
        self.ns[x][y][z] = 1

    def unsetCell(self, x: int, y: int, z: int) -> None:

        if self.ns[x][y][z]:
            self.cnt[x] -= 1
        self.ns[x][y][z] = 0

    def largestMatrix(self) -> int:

        mx = -inf
        ans = 0
        for i in range(len(self.cnt)):
            if self.cnt[i] >= mx:
                mx = self.cnt[i]
                ans = i

        return ans

# Your Matrix3D object will be instantiated and called as such:
# obj = Matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()