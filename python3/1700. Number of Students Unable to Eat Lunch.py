class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                counter[sandwich] -= 1
            else:
                return counter[0] + counter[1]

        return 0
