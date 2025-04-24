class Solution:

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        a = sum(1 if i <= queryTime else 0 for i in startTime)
        b = sum(1 if i < queryTime else 0 for i in endTime)

        return a - b
