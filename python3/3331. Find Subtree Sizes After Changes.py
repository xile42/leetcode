from typing import List


class Solution:

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)
        new_parent = dict()

        for i in range(n):
            pi = parent[i]
            while pi != -1:
                # if i == 6:
                #     print(i, pi, s[i], s[pi], new_parent)
                if s[pi] == s[i]:
                    new_parent[i] = pi
                    break
                pi = parent[pi]
        # print(parent)
        for k, v in new_parent.items():
            parent[k] = v
        # print(parent)
        count = [0] * n
        for i in range(n):
            pi = parent[i]
            count[i] += 1
            while pi != -1:
                # print(i, pi, count)
                count[pi] += 1
                pi = parent[pi]

        return count


foo = Solution()
print(foo.findSubtreeSizes([-1,10,0,12,10,18,11,12,2,3,2,2,2,0,4,11,4,2,0], "babadabbdabcbaceeda"))