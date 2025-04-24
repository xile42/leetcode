class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idxs = [i for i in range(len(arr) - 1, -1, -1) if arr[i] == 0]
        for idx in idxs:
            arr.insert(idx, 0)
            arr.pop(-1)
