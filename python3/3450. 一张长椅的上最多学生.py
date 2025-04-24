class Solution:

    def maxStudentsOnBench(self, students: List[List[int]]) -> int:

        d = defaultdict(set)
        ans = 0
        for s, b in students:
            d[b].add(s)
            ans = max(ans, len(d[b]))

        return ans
