class Spreadsheet:

    def __init__(self, rows: int):

        self.d = defaultdict(lambda: defaultdict(int))

    def setCell(self, cell: str, value: int) -> None:

        k1 = cell[0]
        k2 = int(cell[1:])
        self.d[k1][k2] = value

    def resetCell(self, cell: str) -> None:

        k1 = cell[0]
        k2 = int(cell[1:])
        self.d[k1][k2] = 0

    def getValue(self, formula: str) -> int:

        v1, v2 = formula[1:].split("+")

        if v1[0].isdigit():
            v1 = int(v1)
        else:
            k1 = v1[0]
            k2 = int(v1[1:])
            v1 = self.d[k1][k2]

        if v2[0].isdigit():
            v2 = int(v2)
        else:
            k1 = v2[0]
            k2 = int(v2[1:])
            v2 = self.d[k1][k2]

        return v1 + v2