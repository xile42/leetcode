class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:

        d = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        n = sorted(score, reverse=True)
        r = {v: i + 1 for i, v in enumerate(n)}
        results = list()
        for i, v in enumerate(score):
            if r[v] in d:
                results.append(d[r[v]])
            else:
                results.append(str(r[v]))

        return results
        
