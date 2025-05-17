class Solution:

    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:

        if k == 0:
            return []

        s = set()
        for i in range(k + 1):
            j = k - i
            s.add(shorter * i + longer * j)

        return sorted(s)
