class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:

        cnt = Counter(arr)
        tar = max(cnt.values())
        for k, v in cnt.items():
            if v == tar:
                return k
