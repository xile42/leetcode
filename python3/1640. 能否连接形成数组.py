class Solution:

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        d = {i[0]: i for i in pieces}
        cur = 0
        while cur < len(arr):
            tar = arr[cur]
            if tar not in d:
                return False
            if d[tar] != arr[cur:cur + len(d[tar])]:
                return False
            cur += len(d[tar])

        return True
