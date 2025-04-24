class Solution:

    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        d = defaultdict(int)
        for i, j in items1 + items2:
            d[i] += j

        return sorted(d.items())
