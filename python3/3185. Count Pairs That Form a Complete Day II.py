class Solution:

    def countCompleteDayPairs(self, hours: List[int]) -> int:

        results = 0
        count = [0] * 24
        for t in hours:
            results += count[(24 - t % 24) % 24]
            count[t % 24] += 1

        return results
