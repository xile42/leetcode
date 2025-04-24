class Solution:

    def divideArray(self, nums: List[int]) -> bool:

        vs = Counter(nums).values()

        return all(not i & 1 for i in vs)
        
