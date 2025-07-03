class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        ans = list()
        for i in range(n // 3):
            sub = nums[i * 3:(i + 1) * 3]
            if sub[-1] - sub[0] > k:
                return list()
            ans.append(sub)

        return ans
