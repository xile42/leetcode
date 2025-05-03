class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        ans = list()
        tar = len(nums) // 3
        for k, v in c.items():
            if v > tar:
                ans.append(k)

        return ans
