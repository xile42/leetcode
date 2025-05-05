class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, v in enumerate(nums):
            self.d[v].append(i)

    def pick(self, target: int) -> int:
        return random.sample(self.d[target], 1)[0]

    # Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)