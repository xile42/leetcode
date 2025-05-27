class Solution:

    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:

        def f(ns1, ns2):

            i = j = 0
            ans = list()
            while i < len(ns1) and j < len(ns2):
                if ns1[i] == ns2[j]:
                    ans.append(ns1[i])
                    i += 1
                    j += 1
                elif ns1[i] < ns2[j]:
                    i += 1
                else:
                    j += 1

            return ans

        cur = f(arrays[0], arrays[1])
        for arr in arrays[2:]:
            cur = f(cur, arr)

        return cur
