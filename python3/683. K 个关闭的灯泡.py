class Solution:

    def kEmptySlots(self, bulbs: List[int], k: int) -> int:

        active = SortedSet()
        cnt = 0
        for i, x in enumerate(bulbs):
            active.add(x)
            cnt += 1
            pos = active.bisect_left(x)
            if pos != cnt - 1:
                x_next = active[pos + 1]
                if x_next - x == k + 1:
                    return i + 1

            if pos != 0:
                x_pre = active[pos - 1]
                if x - x_pre == k + 1:
                    return i + 1

        return -1
