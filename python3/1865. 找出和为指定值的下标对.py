class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):

        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:

        self.c2[self.nums2[index]] -= 1
        self.c2[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:

        ans = 0
        for k, v in self.c1.items():
            ans += v * self.c2[tot - k]

        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)