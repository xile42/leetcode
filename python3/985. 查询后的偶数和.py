class Solution:

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = list()
        cur = sum(x for x in nums if not x & 1)
        for v, i in queries:
            if nums[i] & 1:
                if v & 1:
                    cur += nums[i] + v
            else:
                if not v & 1:
                    cur += v
                else:
                    cur -= nums[i]
            nums[i] += v
            ans.append(cur)

        return ans
