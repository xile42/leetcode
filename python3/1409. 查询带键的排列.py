class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:

        ans = list()
        ns = list(range(1, m + 1))
        for tar in queries:
            for i in range(m):
                if ns[i] == tar:
                    ans.append(i)
                    ns = [ns[i]] + ns[:i] + ns[i + 1:]
                    break

        return ans
