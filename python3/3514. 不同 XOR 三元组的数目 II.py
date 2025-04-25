from typing import List


class Solution:

    def uniqueXorTriplets(self, nums: List[int]) -> int:

        s = set()
        for i in nums:
            for j in nums:
                s.add(i ^ j)

        # if len(s) == 2048:
        #     return len(s)

        ans = set()
        for i in s:
            for j in nums:
                ans.add(i ^ j)
                if len(ans) == 2048:
                    return len(ans)

        return len(ans)


foo = Solution()
print(foo.uniqueXorTriplets(list(range(1500))))
