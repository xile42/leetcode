class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        if k == 0:
            return len(set(nums))

        intervals = list()
        nums.sort()
        for n in nums:
            intervals.append([n - k, n + k])
        ans = 0
        cur_min = -inf
        for s, e in intervals:
            if s > cur_min:
                target = s
                ans += 1
                cur_min = target
                continue
            elif cur_min + 1 <= e:
                target = cur_min + 1
                ans += 1
                cur_min = target
                continue
            else:
                continue

        return ans