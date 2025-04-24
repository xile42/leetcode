class Solution:

    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        pres = list()
        ans = -1
        for n in nums:
            for pre in pres:
                if n + pre < k:
                    ans = max(ans, n + pre)
                    break
            pres.append(n)
            pres.sort(reverse=True)

        return ans
