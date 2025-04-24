class RangeFreqQuery:

    def __init__(self, arr: List[int]):

        self.d = defaultdict(list)
        for i, n in enumerate(arr):
            self.d[n].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:

        ns = self.d[value]
        i = bisect_left(ns, left)
        j = bisect_right(ns, right)

        return j - i


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
