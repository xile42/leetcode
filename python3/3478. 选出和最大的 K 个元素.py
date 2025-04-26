from typing import List
from heapq import *


class Solution:

    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        ns = list()
        n = len(nums1)
        for i in range(n):
            ns.append([nums1[i], nums2[i], i])
        ns.sort(key=lambda x: x[0])

        # print("ns: {}".format(ns))
        ans = [0] * n
        h = list()
        s = 0
        left = 0
        for right in range(1, n):
            a, b, i = ns[right]
            # print("-in- ans: {}, a: {}, b: {}, i: {}, left: {}".format(ans, a, b, i, left))
            while ns[left][0] != a:
                heappush(h, ns[left][1])
                s += ns[left][1]
                if len(h) > k:
                    s -= heappop(h)
                left += 1
            v = 0 if not h else s
            ans[i] = v
            # print("h: {}".format(h))
            # print("-out- ans: {}, a: {}, b: {}, i: {}, left: {}".format(ans, a, b, i, left))

        return ans


foo = Solution()
print(foo.findMaxSum([4,2,1,5,3], [10,20,30,40,50], 2))
