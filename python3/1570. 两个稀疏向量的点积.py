class SparseVector:

    def __init__(self, nums: List[int]):

        self.d = defaultdict(int)
        for i, v in enumerate(nums):
            if v:
                self.d[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        ans = 0
        dd = vec.d
        for k, v in self.d.items():
            ans += v * dd[k]

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)