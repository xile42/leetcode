class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = list()
        q = list()

        for i, num in enumerate(nums):

            while q and q[0][1] < i - k + 1:
                q.pop(0)
            
            if not q:
                q.append([num, i])
            else:
                while q and q[-1][0] <= num:
                    q.pop(-1)
                q.append([num, i])

            if i >= k - 1:
                ans.append(q[0][0])

        return ans
