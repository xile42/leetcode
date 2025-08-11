class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        h = list()
        for b, a in classes:
            heappush(h, (b / a - (b + 1) / (a + 1), b, a))
        for _ in range(extraStudents):
            _, b, a = heappop(h)
            b += 1
            a += 1
            heappush(h, (b / a - (b + 1) / (a + 1), b, a))

        ans = 0
        for _, b, a in h:
            ans += b / a

        return ans / len(classes)
