class Solution:

    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        total = sum(apple)
        acc = list(accumulate(sorted(capacity, reverse=True)))
        idx = bisect_right(acc, total)

        if idx == len(capacity):
            return idx
        if idx == 0:
            return 0 if total == 0 else 1

        return idx if total == acc[idx - 1] else idx + 1
