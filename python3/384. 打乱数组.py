class Solution:

    def __init__(self, nums: List[int]):

        self.ns = nums
        self.cur = self.ns.copy()

    def reset(self) -> List[int]:

        self.cur = self.ns.copy()

        return self.cur

    def shuffle(self) -> List[int]:

        import numpy as np
        np.random.shuffle(self.cur)

        return self.cur

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()