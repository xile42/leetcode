class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ns = [[x ** 2 + y ** 2, [x, y]] for x, y in points]
        ns.sort(key=lambda x: x[0])
        ns = ns[:k]

        return [i[1] for i in ns]
