class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = Counter(nums)
        ns = sorted(c.items(), key=lambda x: x[-1], reverse=True)

        return [i[0] for i in ns[:k]]
