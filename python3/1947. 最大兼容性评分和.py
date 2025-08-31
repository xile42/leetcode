class Solution:

    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        m, n = len(students), len(students[0])
        dis = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                dis[i][j] = sum(students[i][k] == mentors[j][k] for k in range(n))

        ans = 0
        students_idxs = list(range(m))
        for mentors_idxs in permutations(range(m)):
            ans = max(ans, sum(dis[students_idx][mentors_idx] for students_idx, mentors_idx in zip(students_idxs, mentors_idxs)))

        return ans
