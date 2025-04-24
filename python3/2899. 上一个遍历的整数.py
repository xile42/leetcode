class Solution:


    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:

        seen = list()
        ans = list()

        cnt = 0
        for n in nums:
            if n != -1:
                cnt = 0
                seen = [n] + seen
                continue
            cnt += 1
            if cnt <= len(seen):
                ans.append(seen[cnt - 1])
            else:
                ans.append(-1)

        return ans
