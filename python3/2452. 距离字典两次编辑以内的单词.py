class Solution:

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        ans = list()
        for q in queries:
            for d in dictionary:
                if sum(i != j for i, j in zip(q, d)) <= 2:
                    ans.append(q)
                    break

        return ans
