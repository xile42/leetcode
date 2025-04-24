class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.ns = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:

        idx = bisect.bisect_left(self.ns, val)
        self.ns.insert(idx, val)

        if len(self.ns) >= self.k:
            return self.ns[-self.k]
