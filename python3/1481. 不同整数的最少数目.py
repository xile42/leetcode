class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        cnt = Counter(arr)
        kvs = sorted(cnt.items(), key=lambda x: x[-1])
        ans = 0
        idx = 0
        while idx < len(kvs) and kvs[idx][-1] <= k:
            ans += 1
            k -= kvs[idx][-1]
            idx += 1

        return len(cnt) - ans
