class Solution:

    def findLongestSubarray(self, array: List[str]) -> List[str]:

        cnt = dict()
        cnt[0] = -1
        ans = 0
        ans_ij = None
        cur = 0
        for i, c in enumerate(array):
            cur += 1 if c.isalpha() else -1
            if cur in cnt and i - cnt[cur] > ans:
                ans = i - cnt[cur]
                ans_ij = [cnt[cur], i]
            if cur not in cnt:
                cnt[cur] = i

        return list() if ans_ij is None else array[ans_ij[0] + 1: ans_ij[1] + 1]
