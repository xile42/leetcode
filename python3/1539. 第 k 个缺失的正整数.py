class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:

        s = set(arr)
        cnt = 0
        for i in count(1):
            if i not in s:
                cnt += 1
                if cnt == k:
                    return i
