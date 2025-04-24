class Solution:

    def takeAttendance(self, records: List[int]) -> int:

        s = set(records)
        for i in range(len(records) + 1):
            if i not in s:
                return i
