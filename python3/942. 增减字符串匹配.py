class Solution:

    def diStringMatch(self, s: str) -> List[int]:

        ns = list(range(len(s) + 1))
        results = list()
        for char in s:
            if char == "I":
                results.append(ns[0])
                ns = ns[1:]
            else:
                results.append(ns[-1])
                ns = ns[:-1]
        results.append(ns[0])

        return results
