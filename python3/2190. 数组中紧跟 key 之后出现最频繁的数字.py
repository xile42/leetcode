class Solution:

    def mostFrequent(self, nums: List[int], key: int) -> int:

        c = Counter([nums[i] for i in range(1, len(nums)) if nums[i - 1] == key])
        mx = max(c.values())
        for k, v in c.items():
            if v == mx:
                return k
        
