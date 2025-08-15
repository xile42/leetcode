class Solution:

    def maxPrice(self, items: List[List[int]], capacity: int) -> float:

        if sum([w for _, w in items]) < capacity:
            return -1

        h = list()
        for p, w in items:
            heappush(h, (-p / w, p, w))

        ans = 0
        cur = capacity
        while cur:
            r, p, w = heappop(h)
            if w <= cur:
                ans += p
                cur -= w
            else:
                ans += -r * cur
                cur = 0

        return ans
