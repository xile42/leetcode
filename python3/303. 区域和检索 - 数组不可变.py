class NumArray:


    def __init__(self, nums: List[int]):

        self.acc = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:

        return self.acc[right + 1] - self.acc[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
