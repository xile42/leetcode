class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
        ans_l, ans_r = -inf, inf
        empty = len(nums)
        cnt = [0] * empty
        left = 0
        for r, i in pairs:
            if cnt[i] == 0:  # 包含 nums[i] 的数字
                empty -= 1
            cnt[i] += 1
            while empty == 0:  # 每个列表都至少包含一个数
                l, i = pairs[left]
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r
                cnt[i] -= 1
                if cnt[i] == 0:  # 不包含 nums[i] 的数字
                    empty += 1
                left += 1
        return [ans_l, ans_r]
