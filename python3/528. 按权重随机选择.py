class Solution:

    def __init__(self, w: List[int]):

        self.acc = list(accumulate(w))


    def pickIndex(self) -> int:

        n = random.randint(1, self.acc[-1])
        i = bisect_left(self.acc, n)

        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()