class Solution:

    def minSetSize(self, arr: List[int]) -> int:

        acc = list(accumulate(sorted(Counter(arr).values(), reverse=True)))
        n = len(arr) // 2
        idx = bisect_left(acc, n)

        return idx + 1
